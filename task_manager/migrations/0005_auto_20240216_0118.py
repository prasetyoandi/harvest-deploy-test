# Generated by Django 3.1.14 on 2024-02-15 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_project_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='finishing',
            field=models.CharField(choices=[('TTANPAF', 'Tanpa Finishing'), ('POTONGJADI', 'Potong Jadi'), ('POND', 'Pond'), ('UV', 'Uv Vernish'), ('HOTPRINT', 'Hot Print'), ('KLEMSENG', 'Klemseng'), ('SPIRAL', 'Spiral'), ('EMBOSH', 'Embosh'), ('KANTONG', 'Kantongan'), ('RIT', 'Rit')], max_length=200),
        ),
    ]
