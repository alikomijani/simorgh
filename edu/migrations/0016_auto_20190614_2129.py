# Generated by Django 2.2.1 on 2019-06-14 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu', '0015_auto_20190531_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='father_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='نام پدر'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='father_name',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='نام پدر'),
        ),
    ]
