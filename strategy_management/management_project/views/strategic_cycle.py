from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from management_project.models import StrategicCycle
from management_project.forms import StrategicCycleForm
from management_project.services.permission import role_required, get_user_permissions

@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='strategic_cycle', action='view')
def strategic_cycle_list(request):
    """
    List all strategic cycles for the current user's organization
    """
    permissions = get_user_permissions(request.user)
    cycles = StrategicCycle.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('start_date')

    context = {
        'strategic_cycles': cycles,
        'permissions': permissions,
    }
    return render(request, 'strategic_cycle/list.html', context)


@login_required
@role_required(['editor', 'owner', 'admin'], model_name='strategic_cycle', action='create')
def create_strategic_cycle(request):
    permissions = get_user_permissions(request.user)
    next_url = request.GET.get("next") or request.POST.get("next")  # child URL to return to

    if request.method == "POST":
        form = StrategicCycleForm(request.POST)
        if form.is_valid():
            cycle = form.save(commit=False)
            cycle.organization_name = request.user.organization_name
            cycle.save()
            messages.success(request, "Strategic Cycle created successfully!")

            # Redirect back to child form with new cycle preselected
            if next_url:
                separator = '&' if '?' in next_url else '?'
                return redirect(f"{next_url}{separator}cycle={cycle.pk}")

            return redirect("strategic_cycle_list")  # fallback
    else:
        form = StrategicCycleForm()

    return render(request, "strategic_cycle/form.html", {
        "form": form,
        "next": next_url,
        "permissions": permissions,
    })


@login_required
@role_required(['editor', 'owner', 'admin'], model_name='strategic_cycle', action='edit')
def update_strategic_cycle(request, pk):
    """
    Update an existing strategic cycle
    """
    permissions = get_user_permissions(request.user)
    cycle = get_object_or_404(
        StrategicCycle,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = StrategicCycleForm(request.POST, instance=cycle)
        if form.is_valid():
            form.save()
            messages.success(request, "Strategic cycle updated successfully!")
            return redirect('strategic_cycle_list')
    else:
        form = StrategicCycleForm(instance=cycle)

    context = {
        'form': form,
        'edit_mode': True,
        'editing_strategic_cycle': cycle,
        'permissions': permissions,
    }
    return render(request, 'strategic_cycle/form.html', context)


@login_required
@role_required(['owner', 'admin'], model_name='strategic_cycle', action='delete')
def delete_strategic_cycle(request, pk):
    """
    Delete a strategic cycle belonging to the user's organization
    """
    permissions = get_user_permissions(request.user)
    cycle = get_object_or_404(
        StrategicCycle,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        cycle.delete()
        messages.success(request, "Strategic cycle deleted successfully!")
        return redirect('strategic_cycle_list')

    context = {
        'strategic_cycle': cycle,
        'permissions': permissions,
    }
    return render(request, 'strategic_cycle/delete_confirm.html', context)