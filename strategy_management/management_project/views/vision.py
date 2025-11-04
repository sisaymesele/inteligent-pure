from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from management_project.models import Vision
from management_project.forms import VisionForm
from management_project.services.permission import role_required, get_user_permissions


# -------------------- VISION LIST --------------------
@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='vision', action='view')
def vision_list(request):
    visions = Vision.objects.filter(
        organization_name=request.user.organization_name
    ).order_by('-id')

    form = VisionForm()  # No request needed
    permissions = get_user_permissions(request.user)

    context = {
        'visions': visions,
        'form': form,
        'permissions': permissions,
    }
    return render(request, 'vision/list.html', context)


# -------------------- CREATE VISION --------------------
@login_required
@role_required(['editor', 'owner', 'admin'], model_name='vision', action='create')
def create_vision(request):
    if request.method == 'POST':
        form = VisionForm(request.POST)
        if form.is_valid():
            vision = form.save(commit=False)
            vision.organization_name = request.user.organization_name
            vision.save()
            messages.success(request, "Vision created successfully!")
            return redirect('vision_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = VisionForm()

    permissions = get_user_permissions(request.user)
    visions = Vision.objects.filter(organization_name=request.user.organization_name).order_by('-id')

    return render(request, 'vision/list.html', {
        'form': form,
        'visions': visions,
        'permissions': permissions
    })


# -------------------- UPDATE VISION --------------------
@login_required
@role_required(['editor', 'owner', 'admin'], model_name='vision', action='edit')
def update_vision(request, pk):
    vision = get_object_or_404(
        Vision,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = VisionForm(request.POST, instance=vision)
        if form.is_valid():
            form.save()
            messages.success(request, "Vision updated successfully!")
            return redirect('vision_list')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = VisionForm(instance=vision)

    permissions = get_user_permissions(request.user)
    visions = Vision.objects.filter(organization_name=request.user.organization_name).order_by('-id')

    context = {
        'form': form,
        'visions': visions,
        'edit_mode': True,
        'editing_vision': vision,
        'permissions': permissions,
    }
    return render(request, 'vision/list.html', context)


# -------------------- DELETE VISION --------------------
@login_required
@role_required(['owner', 'admin'], model_name='vision', action='delete')
def delete_vision(request, pk):
    vision = get_object_or_404(
        Vision,
        pk=pk,
        organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        vision.delete()
        messages.success(request, "Vision deleted successfully!")
        return redirect('vision_list')

    permissions = get_user_permissions(request.user)
    return render(request, 'vision/delete_confirm.html', {
        'vision': vision,
        'permissions': permissions
    })
