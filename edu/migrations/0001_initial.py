# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-12 06:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level',
                 models.CharField(choices=[('1', 'پایه اول'), ('2', 'پایه دوم'), ('3', 'پایه سوم')], max_length=1)),
                ('group', models.CharField(choices=[('A', 'کلاس الف'), ('B', 'کلاس ب')], max_length=1)),
                ('field', models.CharField(choices=[('HU', 'علوم انسانی'), ('MA', 'علوم ریاضی'), ('NA', 'علوم تجربی')],
                                           max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField()),
                ('classroom',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.Classroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_id', models.IntegerField()),
                ('hire_date', models.DateField()),
                ('education_degree', models.CharField(
                    choices=[('FD', 'کاردانی'), ('LI', 'لیسانس'), ('FL', 'فوق لیسانس'), ('DR', 'دکتری'),
                             ('DI', 'دیپلم')], max_length=2)),
                ('classroom', models.ManyToManyField(to='edu.Classroom')),
                ('profession',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
