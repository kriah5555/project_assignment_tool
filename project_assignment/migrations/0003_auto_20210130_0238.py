# Generated by Django 3.1.5 on 2021-01-29 21:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_assignment', '0002_auto_20210130_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 30, 2, 38, 10, 878358)),
        ),
        migrations.AlterField(
            model_name='employees',
            name='date_of_joining',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 30, 2, 38, 10, 878358)),
        ),
        migrations.AlterField(
            model_name='employees',
            name='gender',
            field=models.CharField(choices=[('MAle', 'MALE'), ('FEMALE', 'FEMALE'), ('GAY', 'GAY')], default='MALE', max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_end_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 30, 2, 38, 10, 878358)),
        ),
        migrations.AlterField(
            model_name='project',
            name='projedct_start_time',
            field=models.DateField(blank=True, default=datetime.datetime(2021, 1, 30, 2, 38, 10, 878358)),
        ),
    ]
