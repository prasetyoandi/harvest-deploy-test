import datetime
import json
import random

from django.contrib.auth.models import User
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View

from reports.models import ProjectInfo
from .models import Task, Project, KalkulatorCetak


class Projects(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        list = []

        for p in projects:
            if p.owner == user or user.id in p.get_members():
                list.append(ProjectInfo(p))

        paper_choices = Project.paper_choice
        gram_choices = Project.gram_choice
        laminasi_choices = Project.laminasi_choice
        finishing_choices = Project.finishing_choice
        sisi_choices = Project.sisi_choice
        ukuran_bahan_choices = Project.ukuran_bahan_choice

        data = {"user": user,
                "first": user.username[0],
                "other_users": User.objects.filter(~Q(id=user.id)).all(),
                "projects": list,
                "paper": paper_choices,
                "gramatur": gram_choices,
                "laminasi": laminasi_choices,
                "finishing": finishing_choices,
                "sisi": sisi_choices,
                "ukuran_bahan": ukuran_bahan_choices
                }
        return render(request, 'projects.html', data)

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('signIn')

        name = request.POST['name']
        kode = request.POST['kode']
        date_spk = request.POST['spk']
        date_deadline = request.POST['deadline']

        paper = request.POST['paper']
        gramatur = request.POST['gramatur']
        laminasi = request.POST['laminasi']
        finishing = request.POST.getlist('finishing', [])
        sisi = request.POST['sisi']

        jumlah_plat = request.POST['jumlah_plat']
        uk_bahan_cetak = request.POST['uk_bahan_cetak']
        jumlah_cetak = request.POST['jumlah_cetak']
        jumlah_waste = request.POST['jumlah_waste']
        jumlah_kertas = request.POST['jumlah_kertas']
        ukuran_bahan = request.POST['ukuran_bahan']
        owner = request.user
        user_ids = request.POST.getlist('users', [])

        ids = []
        for id in user_ids:
            ids.append(int(id))

        n = random.randint(1, 3)
        pf_url = f'/media/project-logos/{n}.png'

        proj = Project.objects.create(
            name=name,
            kode=kode,
            date_spk=date_spk,
            date_deadline=date_deadline,
            paper=paper,
            gramatur=gramatur,
            laminasi=laminasi,
            finishing=finishing,
            sisi=sisi,
            jumlah_plat=jumlah_plat,
            uk_bahan_cetak=uk_bahan_cetak,
            jumlah_cetak=jumlah_cetak,
            jumlah_waste=jumlah_waste,
            jumlah_kertas=jumlah_kertas,
            ukuran_bahan=ukuran_bahan,
            owner=owner,
            members=json.dumps(ids),
            profile_photo=pf_url
        )
        proj.save()

        return redirect('boards')


class MangeProject(View):
    def post(self, request, id):
        Project.objects.filter(id=id).delete()

        response = JsonResponse({"message": "OK"})
        response.status_code = 200
        return response

# class KalkulatorCetaks(View):
#     def get(self, request, id):
#         if not request.user.is_authenticated:
#             return redirect("signIn")
        
#         kal = KalkulatorCetak.objects.all()
#         print(f"kal: {kal}")
#         user = request.user
#         users = User.objects.filter(Q(id__in=kal.get_members()) | Q(id=kal.owner.id))
#         data = {"user": user,
#                 "first": user.username[0],
#                 "other_users": users,
#                 "kalkulatorcetaks": kal.task_set.all(),
#                 'kal': kal
#                 }
#         return render(request, 'calculate.html', data)
    
#     def post(self, request, id):
#         if not request.user.is_authenticated:
#             return redirect('signIn')
        
#         tipe_kertas = 'ap'
#         gramatur_kertas = '80'
#         ukuran_kertas = 'a4'

#         kalkulatorcetak = KalkulatorCetak(tipe_kertas=tipe_kertas, gramatur_kertas=gramatur_kertas,
#                     ukuran_kertas=ukuran_kertas)
#         kalkulatorcetak.save()

#         return redirect('kalkulatorcetaks', id=id)


class Tasks(View):
    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect("signIn")

        proj = Project.objects.filter(id=id).first()
        print(f"proj: {proj}")
        user = request.user
        users = User.objects.filter(Q(id__in=proj.get_members()) | Q(id=proj.owner.id))
        data = {"user": user,
                "first": user.username[0],
                "other_users": users,
                "tasks": proj.task_set.all(),
                'proj': proj,
                "can_add": user == proj.owner
                }
        return render(request, 'tasks.html', data)

    def post(self, request, id):
        if not request.user.is_authenticated:
            return redirect('signIn')

        assigned_to = request.POST['users']
        status = 'T'
        end_time = request.POST['date']

        task = Task(assigned_to_id=assigned_to, status=status,
                    end_time=end_time, project_id=id)
        task.save()

        return redirect('tasks', id=id)


class ManegeTasks(View):
    def post(self, request, id):
        print('Received POST request to ManegeTasks view')
        print('Request POST data:', request.POST)
        if not request.user.is_authenticated:
            response = JsonResponse({"error": "Invalid User"})
            response.status_code = 403
            return response

        user = request.user
        type = request.POST['type']

        if type == 'edit_status':
            task_id = request.POST['task_id']
            status = request.POST['board_id']
            task = Task.objects.filter(id=task_id).first()

            if status in ['O', 'B', 'L'] or task.status in ['O', 'B', 'L']:
                if user == task.project.owner:
                    task.status = status
                    task.save()

                else:
                    response = JsonResponse({"error": "You Do Not Have Permission"})
                    response.status_code = 403
                    return response
            else:
                if user == task.assigned_to or user == task.project.owner:
                    task.status = status
                    if status == 'D':
                        task.start_time = datetime.datetime.today().date()
                    task.save()
                else:
                    response = JsonResponse({"error": "You Do Not Have Permission"})
                    response.status_code = 403
                    return response

            response = JsonResponse({"message": "OK"})
            response.status_code = 200
            return response
        
        elif type == 'change_status':
            task_id = request.POST['task_id']
            new_status = request.POST['new_status']
            try:
                task = Task.objects.get(id=task_id)
                if new_status and new_status in [choice[0] for choice in Task.status_choices]:
                    task.status = new_status
                    task.save()
                    return JsonResponse({'success': True})
                else:
                    return JsonResponse({'success': False, 'error': 'Invalid status'})
            except Task.DoesNotExist:
                return JsonResponse({'success': False, 'error': 'Task not found'})
            except Exception as e:
                return JsonResponse({'success': False, 'error': str(e)})

        if type == 'edit_end_time':

            task_id = request.POST['task_id']
            end_time = request.POST['new_end_time']

            task = Task.objects.filter(id=task_id).first()

            if user == task.project.owner:
                task.end_time = end_time
                task.save()

                response = JsonResponse({"message": "OK"})
                response.status_code = 200
                return response

            else:
                response = JsonResponse({"error": "You Do Not Have Permission"})
                response.status_code = 403
                return response
