# Generated by Django 3.2.25 on 2024-05-06 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculate', '0013_auto_20240503_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricedata',
            name='ukuran_kertas',
            field=models.CharField(choices=[('623.7', 'A4'), ('1247.4', 'A3')], max_length=50),
        ),
    ]
