from django.db import models
from task_manager.models import Project, Task, User, KalkulatorCetak

PAPER_SIZE_CHOICES = [
    ('1617', '31 x 49'),
    ('2144', '31.5 x 64'),
    ('3072', '48 x 64'),
    ('6500', '65 x 100'),
    ('1782', '33 x 54'),
    ('3519', '51 x 69'),
    ('1254', '33 x 38'),
    ('1419', '33 x 43'),
    ('2014', '38 x 53'),
    ('2518.5', '34.5 x 73'),
    ('2584', '38 x 68'),
    ('3723', '51 x 73'),
    ('4134', '53 x 78'),
    ('8611', '79 x 109'),
]

class PriceData(models.Model):
    tipe_kertas = models.CharField(max_length=50)
    ukuran_kertas = models.CharField(max_length=50, choices=PAPER_SIZE_CHOICES)  # Paper size
    harga = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit

    def __str__(self):
        return f"{self.tipe_kertas} - {self.ukuran_kertas} - Rp{self.harga}"

MESIN_CHOICES = [
    ('300000', '0V 52'),
    ('350000', '0V 58'),
    ('450000', '0V 66'),
    ('500000', '0V 72'),
]

class ProductionPrice(models.Model):
    production_cost = models.CharField(max_length=50, choices=MESIN_CHOICES)
    set_warna = models.CharField(max_length=50)
    harga_produksi = models.DecimalField(max_digits=10, decimal_places=2)  # Price per uni

    def __str__(self):
        return f"{self.production_cost} - {self.set_warna} - Rp{self.harga_produksi}"
    
class DregCost(models.Model):
    jumlah_dreg = models.DecimalField(max_digits=10, decimal_places=2)
    ukuran_dreg = models.DecimalField(max_digits=10, decimal_places=2, choices=[(0, 'Tanpa Dreg'), (110, '110'), (120, '120')])
    harga_dreg = models.DecimalField(max_digits=10, decimal_places=2)
    
class LaminateCost(models.Model):
    laminate_type = models.DecimalField(max_digits=10, decimal_places=2, choices=[(0, 'No Laminate'), (0.15, '0.15'), (0.2, '0.2')])
    harga_laminasi = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.get_laminate_type_display()} - Rp{self.harga_laminasi}"
    
class FinishingCost(models.Model):
    tipe_finishing = models.CharField(max_length=50)
    harga_finishing = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.tipe_finishing} - Rp{self.harga_finishing}"



class ProjectInfo:
    def __init__(self, project):
        self.project = project.paper


        self.project = project
        self.name = project.name
        all_tasks = project.task_set.all()
        self.users = []

        self.tasks = len(all_tasks)
        for id in project.get_members():
            user = User.objects.filter(id=id).first()
            self.users.append(user)

        self.t = 0
        self.d = 0
        self.i = 0
        self.o = 0

        for task in all_tasks:
            if task.status == 'T':
                self.t = self.t + 1

            elif task.status == 'D':
                self.d = self.d + 1

            elif task.status == 'I':
                self.i = self.i + 1

            elif task.status == 'O':
                self.o = self.o + 1

        all_tasks = self.t + self.d + self.i + self.o

        if all_tasks != 0:
            self.progress = int((self.o * 100) / all_tasks)
        else:
            self.progress = 0


class UserInfo:
    def __init__(self, user):
        self.user = user
        self.todo = 0
        self.doing = 0
        self.done = 0
        self.progress = 0

    def analyze_project(self, project):
        all_tasks = project.task_set.all()
        for task in all_tasks:
            if task.assigned_to == self.user:
                if task.status == 'T':
                    self.todo = self.todo + 1

                elif task.status == 'D':
                    self.doing = self.doing + 1

                elif task.status == 'I':
                    self.doing = self.doing + 1

                elif task.status == 'O':
                    self.done = self.done + 1

        all_tasks = self.todo + self.doing + self.done

        if all_tasks != 0:
            self.progress = int((self.done * 100) / all_tasks)
        else:
            self.progress = 0


class UserInProject:
    def __init__(self, user, project):
        self.u_info = UserInfo(user)
        self.name = project.name
        self.paper = project.paper
        self.u_info.analyze_project(project)
