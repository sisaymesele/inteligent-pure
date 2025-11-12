from django.shortcuts import render, redirect, get_object_or_404
from management_project.models import StrategyHierarchy
from management_project.forms import StrategyHierarchyForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render
from management_project.services.permission import role_required, get_user_permissions

#

#

from django.db.models import Case, When, IntegerField

@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='strategy_hierarchy', action='view')
def strategy_hierarchy_list(request):
    """
    List all strategy hierarchy entries for the logged-in user's organization,
    with optional search on perspective, focus area, and objective,
    ordered by perspective (custom order) and preserving focus area & objective order.
    """
    permissions = get_user_permissions(request.user)

    # Base queryset filtered by user's organization
    strategies = StrategyHierarchy.objects.filter(
        organization_name=request.user.organization_name
    )

    # Get search query
    query = request.GET.get('q', '')
    if query:
        strategies = strategies.filter(
            Q(strategic_perspective__icontains=query) |
            Q(focus_area__icontains=query) |
            Q(objective__icontains=query)
        )

    # If no strategies exist, show empty state
    if not strategies.exists():
        context = {
            'strategy_list': [],
            'strategies': strategies,
            'has_data': False,
            'query': query,
            'permissions': permissions,
        }
        return render(request, 'strategy_hierarchy/list.html', context)

    # Determine perspective order based on organization classification
    classification = strategies.first().organization_name.organization_classification
    if classification == 'profitable':
        perspectives_order = [
            "Financial Perspective",
            "Customer Perspective",
            "Internal Process Perspective",
            "Learning & Growth Perspective",
        ]
    else:
        perspectives_order = [
            "Customer Perspective",
            "Financial Perspective",
            "Internal Process Perspective",
            "Learning & Growth Perspective",
        ]

    # Annotate numeric order for custom perspective ordering
    cases = [When(strategic_perspective=persp, then=pos) for pos, persp in enumerate(perspectives_order)]
    strategies = strategies.annotate(
        perspective_order=Case(*cases, output_field=IntegerField())
    ).order_by('perspective_order', 'focus_area', 'objective')  # order by custom perspective, then focus area, then objective

    # Build grouped strategy list by perspective
    strategy_list = []
    for perspective_name in perspectives_order:
        perspective_strategies = strategies.filter(strategic_perspective=perspective_name)

        if perspective_strategies.exists():
            perspective_data = {
                'name': perspective_name,
                'strategies': []
            }
            for strategy in perspective_strategies:
                perspective_data['strategies'].append({
                    'focus_area': strategy.focus_area,
                    'objective': strategy.objective
                })
            strategy_list.append(perspective_data)

    context = {
        'strategy_list': strategy_list,  # grouped by perspective
        'strategies': strategies,        # full queryset, now correctly ordered
        'has_data': True,
        'query': query,
        'permissions': permissions,
    }

    return render(request, 'strategy_hierarchy/list.html', context)



@login_required
@role_required(['editor', 'owner', 'admin'], model_name='strategy_hierarchy', action='create')
def create_strategy_hierarchy(request):
    permissions = get_user_permissions(request.user)
    next_url = request.GET.get('next') or request.POST.get('next')

    if request.method == 'POST':
        form = StrategyHierarchyForm(request.POST, request=request)
        if 'save' in request.POST and form.is_valid():
            strategy = form.save(commit=False)
            strategy.organization_name = request.user.organization_name
            strategy.save()
            messages.success(request, "Strategy hierarchy created successfully!")

            if next_url:
                separator = '&' if '?' in next_url else '?'
                return redirect(f"{next_url}{separator}strategy_hierarchy={strategy.pk}")

            return redirect('strategy_hierarchy_list')
    else:
        form = StrategyHierarchyForm(request=request)

    return render(request, 'strategy_hierarchy/form.html', {
        'form': form,
        'next': next_url,
        'permissions': permissions,
    })


@login_required
@role_required(['editor', 'owner', 'admin'], model_name='strategy_hierarchy', action='edit')
def update_strategy_hierarchy(request, pk):
    permissions = get_user_permissions(request.user)
    entry = get_object_or_404(
        StrategyHierarchy,
        pk=pk,
        organization_name=request.user.organization_name
    )

    next_url = request.GET.get('next') or request.POST.get('next')

    if request.method == 'POST':
        form = StrategyHierarchyForm(request.POST, instance=entry, request=request)
        if 'save' in request.POST and form.is_valid():
            form.save()
            messages.success(request, "Strategy hierarchy updated successfully!")

            if next_url:
                separator = '&' if '?' in next_url else '?'
                return redirect(f"{next_url}{separator}strategy_hierarchy={entry.pk}")

            return redirect('strategy_hierarchy_list')
    else:
        form = StrategyHierarchyForm(instance=entry, request=request)

    return render(request, 'strategy_hierarchy/form.html', {
        'form': form,
        'next': next_url,
        'permissions': permissions,
    })



@login_required
@role_required(['owner', 'admin'], model_name='strategy_hierarchy', action='delete')
def delete_strategy_hierarchy(request, pk):
    """
    Delete an existing strategy hierarchy entry, only if it belongs to the user's organization.
    """
    permissions = get_user_permissions(request.user)
    entry = get_object_or_404(
        StrategyHierarchy,
        pk=pk,
        organization_name=request.user.organization_name
    )
    if request.method == 'POST':
        entry.delete()
        messages.success(request, "Strategy hierarchy deleted successfully!")
        return redirect('strategy_hierarchy_list')

    return render(request, 'strategy_hierarchy/delete_confirm.html', {
        'entry': entry,
        'permissions': permissions,
    })



@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='strategy_hierarchy', action='view')
def strategy_map(request):
    """
    Generate a strategy map for the logged-in user's organization,
    grouped by perspective and objective.
    """
    permissions = get_user_permissions(request.user)

    # Filter strategies by user's organization
    strategies = StrategyHierarchy.objects.filter(
        organization_name=request.user.organization_name
    ).select_related('organization_name')

    # If no strategies exist, show empty state
    if not strategies.exists():
        context = {
            'strategy_list': [],
            'has_data': False,
            'permissions': permissions,
        }
        return render(request, 'strategy_hierarchy/map.html', context)

    # Get organization classification
    classification = strategies.first().organization_name.organization_classification

    # Set perspective order based on classification
    if classification == 'profitable':
        perspectives_order = [
            "Financial Perspective",
            "Customer Perspective",
            "Internal Process Perspective",
            "Learning & Growth Perspective",
        ]
    else:
        perspectives_order = [
            "Customer Perspective",
            "Financial Perspective",
            "Internal Process Perspective",
            "Learning & Growth Perspective",
        ]

    # Build strategy data
    strategy_list = []
    for perspective_name in perspectives_order:
        perspective_strategies = strategies.filter(strategic_perspective=perspective_name)

        if perspective_strategies.exists():
            perspective_data = {
                'name': perspective_name,
                'objectives': []
            }

            # Get unique objectives for this perspective
            objectives_data = {}
            for strategy in perspective_strategies:
                if strategy.objective not in objectives_data:
                    objectives_data[strategy.objective] = {
                        'name': strategy.objective,
                    }

            perspective_data['objectives'] = list(objectives_data.values())
            strategy_list.append(perspective_data)

    context = {
        'strategy_list': strategy_list,
        'has_data': True,
        'permissions': permissions,
    }

    return render(request, 'strategy_hierarchy/map.html', context)



