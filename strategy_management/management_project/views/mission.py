from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from management_project.models import Mission
from management_project.forms import MissionForm
from management_project.services.permission import role_required_invitation, get_user_permissions

# -------------------- MISSION LIST --------------------
@login_required
@role_required_invitation(['viewer', 'editor', 'owner', 'admin'], model_name='mission', action='view')
def mission_list(request):
    """
    List all missions for the logged-in user's organization.
    """
    missions = Mission.objects.filter(organization_name=request.user.organization_name).order_by('-id')

    paginator = Paginator(missions, 10)  # 10 missions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    form = MissionForm()  # Empty form for creating new missions
    permissions = get_user_permissions(request.user)  # For template buttons

    context = {
        'page_obj': page_obj,
        'form': form,
        'permissions': permissions,
    }
    return render(request, 'mission/list.html', context)


# -------------------- CREATE MISSION --------------------
@login_required
@role_required_invitation(['editor', 'owner', 'admin'], model_name='mission', action='create')
def create_mission(request):
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if form.is_valid():
            mission = form.save(commit=False)
            mission.organization_name = request.user.organization_name
            mission.save()
            messages.success(request, "Mission created successfully!")
            return redirect('mission_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MissionForm()

    permissions = get_user_permissions(request.user)
    return render(request, 'mission/list.html', {'form': form, 'permissions': permissions})


# -------------------- UPDATE MISSION --------------------
@login_required
@role_required_invitation(['editor', 'owner', 'admin'], model_name='mission', action='edit')
def update_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = MissionForm(request.POST, instance=mission)
        if form.is_valid():
            form.save()
            messages.success(request, "Mission updated successfully!")
            return redirect('mission_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = MissionForm(instance=mission)

    permissions = get_user_permissions(request.user)
    context = {
        'form': form,
        'edit_mode': True,
        'editing_mission': mission,
        'permissions': permissions,
    }
    return render(request, 'mission/list.html', context)


# -------------------- DELETE MISSION --------------------
@login_required
@role_required_invitation(['owner', 'admin'], model_name='mission', action='delete')
def delete_mission(request, pk):
    mission = get_object_or_404(
        Mission,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        mission.delete()
        messages.success(request, "Mission deleted successfully!")
        return redirect('mission_list')

    permissions = get_user_permissions(request.user)
    return render(request, 'mission/delete_confirm.html', {'mission': mission, 'permissions': permissions})