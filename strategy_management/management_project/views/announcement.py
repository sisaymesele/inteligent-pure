from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from management_project.models import Announcement
from management_project.services.permission import role_required, get_user_permissions


@login_required
@login_required
@role_required(['viewer', 'editor', 'owner', 'admin'], model_name='announcement', action='view')
def announcement_list(request):
    permissions = get_user_permissions(request.user)
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'announcement/list.html',
                  {'announcements': announcements, 'permissions': permissions})

#