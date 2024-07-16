from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from datetime import datetime
from task_manager.models import Project
from .models import ProjectInfo, UserInfo, UserInProject

class Spk(View):
    def get(self, request, project_id=None):
        if not request.user.is_authenticated:
            return redirect('signIn')
        
        user = request.user
        
        if project_id:
            project = get_object_or_404(Project, id=project_id)
            projects = [project]
        else:
            projects = Project.objects.all()
        
        p_info_list = []
        u_info = UserInfo(user)
        user_in_projects = []
        
        for p in projects:
            if p.owner == user or user.id in p.get_members():
                p_info = ProjectInfo(p)
                u_info.analyze_project(p)
                p_info_list.append(p_info)
                user_in_projects.append(UserInProject(user, p))
        
        data = {
            "user": user,
            "first": user.username[0],
            "p_info": p_info_list,
            "u_info": u_info,
            "u_in_p": user_in_projects,
            'time': datetime.today()
        }
        
        return render(request, 'spk.html', data)