from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from management_project.models import OrganizationalProfile, OrganizationInvitation
from management_project.forms import OrganizationalProfileForm
from management_project.services.permission import role_required, get_user_permissions


# --------------------
# List Organizational Profiles
# --------------------
@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='organizational_profile', action='view')
def organizational_profile(request):
    """List all organizational profiles of the user's organization."""
    organizational_profiles = OrganizationalProfile.objects.filter(
        organization_name=request.user.organization_name
    )
    permissions = get_user_permissions(request.user)

    context = {
        'organizational_profiles': organizational_profiles,
        'permissions': permissions,
    }
    return render(request, 'organizational_profile/list.html', context)


# --------------------
# Create Organization
# --------------------
@login_required
def create_organizational_profile(request):
    """Create a new organization; first user becomes owner automatically."""
    # Prevent creating if user already belongs to an accepted invitation
    if OrganizationInvitation.objects.filter(email=request.user.email, status=OrganizationInvitation.ACCEPTED).exists():
        messages.info(request, "You already belong to an organization.")
        return redirect('dashboard')

    if request.method == 'POST':
        form = OrganizationalProfileForm(request.POST)
        if form.is_valid():
            org = form.save()

            # Assign user to this organization
            request.user.organization_name = org
            request.user.save()

            # Automatically create invitation for creator as owner
            OrganizationInvitation.objects.create(
                organization_name=org,
                email=request.user.email,
                role='owner',
                invited_by=request.user,
                status=OrganizationInvitation.ACCEPTED,
                responded_at=timezone.now()
            )

            messages.success(request, "Organization created successfully. You are assigned as Owner.")
            return redirect('dashboard')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = OrganizationalProfileForm()

    permissions = get_user_permissions(request.user)
    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'organizational_profile/form.html', context)


# --------------------
# Update Organization
# --------------------
@login_required
@role_required(['owner', 'admin'], model_name='organizational_profile', action='view')
def update_organizational_profile(request, pk):
    """Update the organizational profile; user can only update their organization."""
    organizational_profile = get_object_or_404(
        OrganizationalProfile, pk=pk, organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        form = OrganizationalProfileForm(request.POST, instance=organizational_profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Organizational Profile updated successfully!")
            return redirect('organizational_profile')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = OrganizationalProfileForm(instance=organizational_profile)

    permissions = get_user_permissions(request.user)
    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': True,
        'editing_profile': organizational_profile,
    }
    return render(request, 'organizational_profile/form.html', context)


# --------------------
# Delete Organization
# --------------------
@login_required
@role_required(['owner', 'admin'], model_name='organizational_profile', action='view')
def delete_organizational_profile(request, pk):
    """Delete an organizational profile; user can only delete their own organization."""
    profile = get_object_or_404(
        OrganizationalProfile, pk=pk, organization_name=request.user.organization_name
    )

    if request.method == "POST":
        profile.delete()
        messages.success(request, "Organizational Profile deleted successfully!")
        return redirect("organizational_profile")

    permissions = get_user_permissions(request.user)
    context = {
        'profile': profile,
        'permissions': permissions,
    }
    return render(request, "organizational_profile/delete_confirm.html", context)
