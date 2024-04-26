from django.db import models
from django.contrib.auth.models import User
import json
from datetime import date

class Project(models.Model):

    kode = models.CharField(max_length=200)
    date_spk = models.DateField()
    date_deadline = models.DateField()

    # for paper
    paper_choice = (
        ('AP', 'Art Paper'),
        ('DUPLEK', 'Duplek'),
        ('IVORY', 'Ivory'),
        ('HVS', 'HVS'),
        ('BONTAC', 'Bontac'),
        ('BC', 'BC TIK')
    )

    paper = models.CharField(max_length=20, choices=paper_choice)

    # for gramatur
    gram_choice = (
        ('80', '80 gsm'),
        ('100', '100 gsm'),
        ('120', '120 gsm'),
        ('150', '150 gsm'),
        ('190', '190 gsm'),
        ('210', '210 gsm'),
        ('230', '230 gsm'),
        ('250', '250 gsm'),
        ('260', '260 gsm'),
        ('300', '300 gsm'),
        ('310', '310 gsm'),
        ('350', '350 gsm'),
        ('400', '400 gsm')
    )

    gramatur = models.CharField(max_length=20, choices=gram_choice)

    # for laminate
    laminasi_choice = (
        ('TANPAL','Tanpa Laminasi'),
        ('GLOSSY','glossy'),
        ('DOFF','doff')
    )

    laminasi = models.CharField(max_length=20, choices=laminasi_choice)

    # for Finishing
    finishing_choice = (
        ('TTANPAF', 'Tanpa Finishing'),
        ('POTONGJADI', 'Potong Jadi'),
        ('POND', 'Pond'),
        ('UV', 'Uv Vernish'),
        ('HOTPRINT', 'Hot Print'),
        ('KLEMSENG', 'Klemseng'),
        ('SPIRAL', 'Spiral'),
        ('EMBOSH', 'Embosh'),
        ('KANTONG', 'Kantongan'),
        ('RIT', 'Rit')
    )

    finishing = models.CharField(max_length=200, choices=finishing_choice)

    # for side plat
    sisi_choice = (
        ('1side', '1 Sisi'),
        ('2side1plate', '2 sisi Balik Plat'),
        ('2side2plate', '2 sisi Ganti Plat')
    )

    sisi = models.CharField(max_length=20, choices=sisi_choice)

    # for ukuran bahan
    ukuran_bahan_choice = (
        ('61x86', '61 x 86'),
        ('65x90', '65 x 90'),
        ('65x100', '65 x 100'),
        ('79x109', '79 x 109'),
        ('70x108', '70 x 108'),
        ('64x96', '64 x 96'),
        ('85x120', '85 x 120'),
        ('65x48', '65 x 48')
    )

    ukuran_bahan = models.CharField(max_length=20, choices=ukuran_bahan_choice)

    name = models.CharField(max_length=50)
    jumlah_plat = models.CharField(max_length=20)
    uk_bahan_cetak = models.CharField(max_length=20)
    jumlah_cetak = models.CharField(max_length=20)
    jumlah_waste = models.CharField(max_length=20)
    jumlah_kertas = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.CharField(max_length=500)
    profile_photo = models.CharField(max_length=200, default='/static/media/project-logos/1.png')

    def get_members(self):
        return json.loads(self.members)
    
class KalkulatorCetak(models.Model):
    JENIS_KERTAS_CHOICES = [
        ('ap', 'Art Paper'),
        ('duplek', 'Duplek'),
        ('ivory', 'Ivory'),
        ('hvs', 'HVS'),
        ('bontac','Bontac'),
        ('bctik', 'BC TIK'),
    ]

    tipe_kertas = models.CharField(max_length=50, choices=JENIS_KERTAS_CHOICES)

    GRAMATUR_CHOICES = [
        ('80', '80 gsm'),
        ('100', '100 gsm'),
        ('120', '120 gsm'),
        ('150', '150 gsm'),
        ('190', '190 gsm'),
        ('210', '210 gsm'),
        ('230', '230 gsm'),
        ('250', '250 gsm'),
        ('260', '260 gsm'),
        ('310', '310 gsm'),
        ('350', '350 gsm'),
        ('400', '400 gsm'),
    ]

    gramatur_kertas = models.CharField(max_length=50, choices=GRAMATUR_CHOICES)

    UKURAN_CHOICES = [
        ('a4', 'A4'),
        ('folio', 'Folio'),
        ('a3', 'A3'),
        ('a3plus', '32 x 48 (A3+)'),
    ]

    ukuran_kertas = models.CharField(max_length=50, choices=UKURAN_CHOICES)

    def __str__(self):
        return self.tipe_kertas  # Customize this for a more informative string representation

class Task(models.Model):    
    # name = models.CharField(max_length=50)
    # description = models.CharField(max_length=200)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status_choices = (
        ('T', 'To Do'),
        ('D', 'Doing'),
        ('I', 'In Test'),
        ('O', 'Done'),
        ('B', 'Blocked'),
        ('L', 'Deleted')
    )
    status = models.CharField(max_length=1, choices=status_choices)
    start_time = models.DateField(null=True)
    end_time = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
