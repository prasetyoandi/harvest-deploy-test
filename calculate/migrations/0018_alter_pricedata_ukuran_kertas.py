# Generated by Django 3.2.25 on 2024-05-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0017_auto_20240506_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='ukuran_kertas',
            field=models.CharField(choices=[('100', 'A4'), ('200', 'A3')], max_length=50),
        ),
    ]