from functools import wraps
from django.http import HttpResponseForbidden
from management_project.models import OrganizationInvitation

# -------------------------------
# Invitation-only access decorator
# -------------------------------
def role_required(allowed_roles, model_name=None, action='view'):
    """
    Strict: Only users with an accepted invitation can access.
    Denies access if no invitation exists.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            org = getattr(request.user, 'organization_name', None)
            if not org:
                return HttpResponseForbidden("No organization is associated with your account.")

            # Must have an accepted invitation
            invitation = OrganizationInvitation.objects.filter(
                email=request.user.email,
                organization_name=org,
                status=OrganizationInvitation.ACCEPTED
            ).first()

            if not invitation:
                return HttpResponseForbidden("You do not have permission (invitation required).")

            role = invitation.role
            if role not in allowed_roles:
                return HttpResponseForbidden("Your role does not allow access.")

            # Optional model + action permission
            if model_name:
                permissions = get_user_permissions(request.user)
                perm_key = f"{model_name}_{action}"
                if not permissions.get(perm_key, False):
                    return HttpResponseForbidden("You do not have permission for this action.")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


# -----------------------------------------
# Invitation-preferred access decorator
# -----------------------------------------
def role_required_invitation(allowed_roles, model_name=None, action='view'):
    """
    Flexible: Checks invitation first, then falls back to user.role.
    Useful for admin/system access or first users.
    """
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            org = getattr(request.user, 'organization_name', None)
            if not org:
                return HttpResponseForbidden("No organization is associated with your account.")

            invitation = OrganizationInvitation.objects.filter(
                email=request.user.email,
                organization_name=org,
                status=OrganizationInvitation.ACCEPTED
            ).first()

            # Use invitation role first, fallback to user.role if no invitation
            role = invitation.role if invitation else getattr(request.user, 'role', None)

            if not role or role not in allowed_roles:
                return HttpResponseForbidden("You do not have permission (role fallback).")

            # Optional model + action permission
            if model_name:
                permissions = get_user_permissions(request.user)
                perm_key = f"{model_name}_{action}"
                if not permissions.get(perm_key, False):
                    return HttpResponseForbidden("You do not have permission for this action.")

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


def get_user_permissions(user):
    """
    Returns a dictionary of permissions based on:
    - Accepted invitation role (preferred)
    - Fallback to user.role if no invitation exists
    Roles hierarchy: viewer < editor < owner < admin
    """

    org = getattr(user, 'organization_name', None)
    org_id = org.id if org else None

    invitation = OrganizationInvitation.objects.filter(
        email=user.email,
        organization_name_id=org_id,
        status=OrganizationInvitation.ACCEPTED
    ).first()


    role = invitation.role if invitation else getattr(user, 'role', None)



    # Models and actions - using underscored names for better readability
    models = [
        'organizational_profile', 'organization_invitation',
        'vision', 'mission', 'values',
        'swot_analysis', 'strategy_hierarchy', 'stakeholder',
        'strategic_cycle', 'strategic_action_plan', 'initiative_planning',
        'initiative_report', 'initiative_resource_item_plan',
        'initiative_resource_item_report', 'strategic_report',
        'swot_report', 'risk_management', 'announcement'

    ]
    actions = ['view', 'create', 'edit', 'delete']

    # Initialize all permissions to False
    permissions = {f"{model}_{action}": False for model in models for action in actions}

    # Assign permissions by role
    if role == 'viewer':
        for model in models:
            permissions[f"{model}_view"] = True

    elif role == 'editor':
        for model in models:
            for action in actions:
                permissions[f"{model}_{action}"] = True


    elif role == 'owner':
        for model in models:
            for action in actions:
                permissions[f"{model}_{action}"] = True

        # Additional owner permissions
        permissions['organizational_profile_view'] = True
        permissions['organizational_profile_edit'] = True
        permissions['organization_invitation_create'] = True
        permissions['organization_invitation_send'] = True

    elif role == 'admin':
        for model in models:
            for action in actions:
                permissions[f"{model}_{action}"] = True

                # Additional owner permissions
        # permissions['organizational_profile_view'] = True
        # permissions['organizational_profile_edit'] = True
        # permissions['organization_invitation_create'] = True
        # permissions['organization_invitation_send'] = True

    if role in ('owner', 'admin'):
        extra_org_perms = [
            'organizational_profile_view',
            'organizational_profile_edit',
            'organization_invitation_create',
            'organization_invitation_send'
        ]
        for perm in extra_org_perms:
            permissions[perm] = True



    return permissions