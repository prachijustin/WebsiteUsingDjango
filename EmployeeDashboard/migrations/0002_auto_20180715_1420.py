# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-07-15 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminDashboard', '0002_auto_20180715_1419'),
        ('EmployeeDashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='admin_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminDashboard.AdminProfile'),
        ),
        migrations.AddField(
            model_name='reportwork',
            name='admin_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AdminDashboard.AdminProfile'),
        ),
        migrations.AddField(
            model_name='reportwork',
            name='work_content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ewcontent', to='AdminDashboard.WorkAssign'),
        ),
        migrations.AddField(
            model_name='reportwork',
            name='work_date',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ewdate', to='AdminDashboard.WorkAssign'),
        ),
        migrations.AddField(
            model_name='reportwork',
            name='work_title',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ewtitle', to='AdminDashboard.WorkAssign'),
        ),
    ]
