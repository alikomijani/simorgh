# Generated by Django 2.2.1 on 2019-06-20 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0017_auto_20190620_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPresence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presence', models.BooleanField(verbose_name='حاضر')),
                ('data', models.DateField(verbose_name='تاریخ')),
                ('class_time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='edu.ClassTime')),
                ('student_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu.StudentCourse')),
            ],
        ),
    ]