# Generated by Django 2.2.1 on 2019-06-20 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0016_auto_20190614_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_day', models.CharField(blank=True, choices=[('SA', 'شنبه'), ('SU', 'یکشنبه'), ('MO', 'دوشنبه'), ('TU', 'سه شنبه'), ('WE', 'چهارشنبه'), ('TH', 'پنجشنبه'), ('FR', 'جمعه')], max_length=2, null=True, verbose_name='روز کلاس')),
                ('class_time', models.CharField(blank=True, choices=[('FI', 'زنگ اول'), ('SE', 'زنگ دوم'), ('TH', 'زنگ سوم'), ('FO', 'زنگ چهارم'), ('FI', 'زنگ پنجم')], max_length=2, null=True, verbose_name='زنگ')),
            ],
        ),
        migrations.RemoveField(
            model_name='teacherclasscourse',
            name='class_day',
        ),
        migrations.RemoveField(
            model_name='teacherclasscourse',
            name='class_time',
        ),
        migrations.AddField(
            model_name='teacherclasscourse',
            name='class_time',
            field=models.ManyToManyField(related_name='teacher_class_course', to='edu.ClassTime', verbose_name='زمان کلاس'),
        ),
    ]