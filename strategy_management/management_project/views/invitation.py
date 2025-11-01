from functools import wraps
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import login

from management_project.models import OrganizationalProfile, OrganizationInvitation
from account.models import CustomUser
from account.forms import CustomUserRegistrationForm
from management_project.forms import OrganizationInvitationForm
from management_project.services.permission import role_required_invitation, get_user_permissions


from threading import Thread
from django.core.mail import send_mail
from django.conf import settings

# ---------------- INVITATION LIST ----------------
@login_required
@role_required_invitation(['viewer', 'editor', 'owner', 'admin'], model_name='organization_invitation', action='view')
def invitation_list(request):
    """List all invitations for the current organization."""
    org = get_object_or_404(OrganizationalProfile, organization_name=request.user.organization_name)
    invitations = org.invitations.all().order_by('-created_at')
    permissions = get_user_permissions(request.user)

    context = {
        'organization': org,
        'invitations': invitations,
        'permissions': permissions,
    }
    return render(request, 'invitation/list.html', context)


# ---------------- SEND INVITATION ----------------
@login_required
@role_required_invitation(['editor', 'owner', 'admin'], model_name='organization_invitation', action='create')
def send_invitation(request):
    """Send invitation if user has permission (fast version)."""
    org = get_object_or_404(OrganizationalProfile, organization_name=request.user.organization_name)

    if request.method == 'POST':
        form = OrganizationInvitationForm(request.POST)
        if form.is_valid():
            invitation = form.save(commit=False)
            invitation.organization_name = org
            invitation.invited_by = request.user
            invitation.save()

            accept_url = request.build_absolute_uri(
                reverse('accept_invitation_token', args=[invitation.token])
            )

            # Send email in a background thread
            def send_invite_email():
                send_mail(
                    subject=f"Invitation to join {org.organization_name}",
                    message=f"You have been invited to join {org.organization_name} as {invitation.role}.\n"
                            f"Click here to accept: {accept_url}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[invitation.email],
                )

            Thread(target=send_invite_email).start()  # non-blocking

            messages.success(request, f"Invitation sent to {invitation.email}")
            return redirect('invitation_list')
    else:
        form = OrganizationInvitationForm()

    permissions = get_user_permissions(request.user)
    context = {
        'form': form,
        'permissions': permissions,
        'edit_mode': False,
    }
    return render(request, 'invitation/form.html', context)



# @login_required
# @role_required_invitation(['editor', 'owner', 'admin'], model_name='organization_invitation', action='create')
# def send_invitation(request):
#     """Send invitation if user has permission."""
#     org = get_object_or_404(OrganizationalProfile, organization_name=request.user.organization_name)
#
#     if request.method == 'POST':
#         form = OrganizationInvitationForm(request.POST)
#         if form.is_valid():
#             invitation = form.save(commit=False)
#             invitation.organization_name = org
#             invitation.invited_by = request.user
#             invitation.save()
#
#             accept_url = request.build_absolute_uri(
#                 reverse('accept_invitation_token', args=[invitation.token])
#             )
#
#             send_mail(
#                 subject=f"Invitation to join {org.organization_name}",
#                 message=f"You have been invited to join {org.organization_name} as {invitation.role}.\n"
#                         f"Click here to accept: {accept_url}",
#                 from_email=settings.DEFAULT_FROM_EMAIL,
#                 recipient_list=[invitation.email],
#             )
#
#             messages.success(request, f"Invitation sent to {invitation.email}")
#             return redirect('invitation_list')
#     else:
#         form = OrganizationInvitationForm()
#
#     permissions = get_user_permissions(request.user)
#     context = {
#         'form': form,
#         'permissions': permissions,
#         'edit_mode': False,
#     }
#     return render(request, 'invitation/form.html', context)


# ---------------- CANCEL INVITATION ----------------
@login_required
@role_required_invitation(['editor', 'owner', 'admin'], model_name='organization_invitation', action='delete')
def cancel_invitation(request, pk):
    """Cancel pending invitation."""
    invitation = get_object_or_404(
        OrganizationInvitation,
        pk=pk,
        organization_name__organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        invitation.status = OrganizationInvitation.CANCELLED
        invitation.responded_at = timezone.now()
        invitation.save()
        messages.success(request, f"Invitation to {invitation.email} cancelled.")
        return redirect('invitation_list')

    permissions = get_user_permissions(request.user)
    context = {
        'invitation': invitation,
        'permissions': permissions,
    }
    return render(request, 'invitation/cancel_confirm.html', context)


# ---------------- DELETE INVITATION ----------------
@login_required
@role_required_invitation(['editor', 'owner', 'admin'], model_name='organization_invitation', action='delete')
def delete_invitation(request, pk):
    """Permanently delete an invitation."""
    invitation = get_object_or_404(
        OrganizationInvitation,
        pk=pk,
        organization_name__organization_name=request.user.organization_name
    )

    if request.method == 'POST':
        invitation.delete()
        messages.success(request, f"Invitation to {invitation.email} deleted.")
        return redirect('invitation_list')

    permissions = get_user_permissions(request.user)
    context = {
        'invitation': invitation,
        'permissions': permissions,
    }
    return render(request, 'invitation/delete_confirm.html', context)


# ---------------- ACCEPT INVITATION ----------------
#
#
#
# def accept_invitation_token(request, token):
#     """Handle accepting an invitation via token link."""
#     invitation = get_object_or_404(OrganizationInvitation, token=token)
#
#     if invitation.status != OrganizationInvitation.PENDING:
#         messages.info(request, "This invitation is no longer valid.")
#         return redirect('/login')
#
#     try:
#         user = CustomUser.objects.get(email=invitation.email)
#         login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#
#         if not getattr(user, 'organization_name', None):
#             user.organization_name = invitation.organization_name
#             user.save()
#
#         invitation.status = OrganizationInvitation.ACCEPTED
#         invitation.responded_at = timezone.now()
#         invitation.save()
#
#         messages.success(request, f"You have joined {invitation.organization_name.organization_name} as {invitation.role}")
#         return redirect('dashboard')
#
#     except CustomUser.DoesNotExist:
#         if request.method == 'POST':
#             form = CustomUserRegistrationForm(request.POST)
#             if form.is_valid():
#                 user = form.save(commit=False)
#                 user.email = invitation.email
#                 user.organization_name = invitation.organization_name
#                 user.save()
#                 login(request, user, backend='django.contrib.auth.backends.ModelBackend')
#
#                 invitation.status = OrganizationInvitation.ACCEPTED
#                 invitation.responded_at = timezone.now()
#                 invitation.save()
#
#                 messages.success(request, f"Account created and joined {invitation.organization_name.organization_name} as {invitation.role}")
#                 return redirect('dashboard')
#         else:
#             form = CustomUserRegistrationForm(initial={'email': invitation.email})
#
#         return render(request, 'invitation/register_from_invite.html', {'form': form})



def accept_invitation_token(request, token):
    """Handle accepting an invitation via token link."""
    invitation = get_object_or_404(OrganizationInvitation, token=token)

    if invitation.status != OrganizationInvitation.PENDING:
        messages.info(request, "This invitation is no longer valid.")
        return redirect('/login')

    try:
        user = CustomUser.objects.get(email=invitation.email)
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')

        if not getattr(user, 'organization_name', None):
            user.organization_name = invitation.organization_name
            user.save()

        invitation.status = OrganizationInvitation.ACCEPTED
        invitation.responded_at = timezone.now()
        invitation.save()

        messages.success(request, f"You have joined {invitation.organization_name.organization_name} as {invitation.role}")
        return redirect('dashboard')

    except CustomUser.DoesNotExist:
        if request.method == 'POST':
            form = CustomUserRegistrationForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.email = invitation.email
                user.organization_name = invitation.organization_name
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')

                invitation.status = OrganizationInvitation.ACCEPTED
                invitation.responded_at = timezone.now()
                invitation.save()

                messages.success(request, f"Account created and joined {invitation.organization_name.organization_name} as {invitation.role}")
                return redirect('dashboard')
        else:
            form = CustomUserRegistrationForm(initial={'email': invitation.email})

        return render(request, 'invitation/register_from_invite.html', {'form': form})
