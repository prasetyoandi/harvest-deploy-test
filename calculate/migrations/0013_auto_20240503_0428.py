# Generated by Django 3.2.25 on 2024-05-03 04:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0012_rename_gramatur_kertas_pricedata_plano_besar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pricedata',
            name='plano_besar',
        ),
        migrations.RemoveField(
            model_name='pricedata',
            name='plano_kecil',
        ),
    ]