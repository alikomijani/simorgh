# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-04-25 11:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0002_auto_20190412_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('1', 'پایه اول'), ('2', 'پایه دوم'), ('3', 'پایه سوم')], max_length=1)),
                ('field', models.CharField(choices=[('HU', 'علوم انسانی'), ('MA', 'علوم ریاضی'), ('NA', 'علوم تجربی')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('final_grade', models.FloatField()),
                ('mid_grade', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='TeacherClassCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_time', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='classroom',
            old_name='group',
            new_name='branch',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='education_degree',
            new_name='edu_degree',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='field',
        ),
        migrations.RemoveField(
            model_name='classroom',
            name='level',
        ),
        migrations.RemoveField(
            model_name='student',
            name='classroom',
        ),
        migrations.AddField(
            model_name='classroom',
            name='education_year',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='unit',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_modified_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='profession',
        ),
        migrations.AddField(
            model_name='teacher',
            name='profession',
            field=models.ManyToManyField(to='edu.Course'),
        ),
        migrations.AddField(
            model_name='teacherclasscourse',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_class_course', to='edu.Classroom'),
        ),
        migrations.AddField(
            model_name='teacherclasscourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_class_course', to='edu.Course'),
        ),
        migrations.AddField(
            model_name='teacherclasscourse',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teacher_class_course', to='edu.Teacher'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_courses', to='edu.Course'),
        ),
        migrations.AddField(
            model_name='studentcourse',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='student_courses', to='edu.Student'),
        ),
        migrations.AddField(
            model_name='register',
            name='classroom',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registers', to='edu.Classroom'),
        ),
        migrations.AddField(
            model_name='register',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='registers', to='edu.Student'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='courses',
            field=models.ManyToManyField(related_name='classrooms', through='edu.TeacherClassCourse', to='edu.Course'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='level_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.LevelField'),
        ),
        migrations.AddField(
            model_name='classroom',
            name='teachers',
            field=models.ManyToManyField(related_name='classrooms', through='edu.TeacherClassCourse', to='edu.Teacher'),
        ),
        migrations.AddField(
            model_name='course',
            name='level_field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.LevelField'),
        ),
        migrations.AddField(
            model_name='student',
            name='classrooms',
            field=models.ManyToManyField(related_name='students', through='edu.Register', to='edu.Classroom'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(related_name='students', through='edu.StudentCourse', to='edu.Course'),
        ),
    ]