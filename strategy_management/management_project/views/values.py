from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from management_project.models import Values
from management_project.forms import ValuesForm
from management_project.services.permission import role_required, get_user_permissions

# -------------------- VALUES LIST --------------------
@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='values', action='view')
def values_list(request):
    """
    List all values for the logged-in user's organization.
    """
    values = Values.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('-id')

    form = ValuesForm()  # Empty form for creating new values
    permissions = get_user_permissions(request.user)

    context = {
        'values': values,
        'form': form,
        'permissions': permissions,
    }
    return render(request, 'values/list.html', context)


# -------------------- CREATE VALUES --------------------
@login_required
@role_required(['editor', 'owner', 'admin'], model_name='values', action='create')
def create_values(request):
    if request.method == 'POST':
        form = ValuesForm(request.POST)
        if form.is_valid():
            value = form.save(commit=False)
            value.organization_name = request.user.organization_name
            value.save()
            messages.success(request, "Value created successfully!")
            return redirect('values_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ValuesForm()

    permissions = get_user_permissions(request.user)
    return render(request, 'values/list.html', {'form': form, 'permissions': permissions})


# -------------------- UPDATE VALUES --------------------
@login_required
@role_required(['editor', 'owner', 'admin'], model_name='values', action='edit')
def update_values(request, pk):
    value = get_object_or_404(
        Values,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = ValuesForm(request.POST, instance=value)
        if form.is_valid():
            form.save()
            messages.success(request, "Value updated successfully!")
            return redirect('values_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ValuesForm(instance=value)

    permissions = get_user_permissions(request.user)
    context = {
        'form': form,
        'edit_mode': True,
        'editing_value': value,
        'permissions': permissions,
    }
    return render(request, 'values/list.html', context)


# -------------------- DELETE VALUES --------------------
@login_required
@role_required(['owner', 'admin'], model_name='values', action='delete')
def delete_values(request, pk):
    value = get_object_or_404(
        Values,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        value.delete()
        messages.success(request, "Value deleted successfully!")
        return redirect('values_list')

    permissions = get_user_permissions(request.user)
    return render(request, 'values/delete_confirm.html', {'value': value, 'permissions': permissions})
