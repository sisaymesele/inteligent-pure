from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from management_project.models import OrganizationalProfile
from management_project.services.permission import role_required, get_user_permissions


@login_required
def dashboard(request):
    # Ensure the user belongs to an organization
    has_company = OrganizationalProfile.objects.filter(
        organization_name=request.user.organization_name
    ).exists()

    if not has_company:
        return redirect('create_organizational_profile')

    # Get permissions for template
    permissions = get_user_permissions(request.user)

    return render(request, 'dashboard.html', {
        'permissions': permissions
    })
