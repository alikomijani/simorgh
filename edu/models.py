from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey('Classroom', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Classroom(models.Model):
    FIRST, SECOND, THIRD = '1', '2', '3',
    CHOICE_LEVEL = (
        (FIRST, 'پایه اول'),
        (SECOND, 'پایه دوم'),
        (THIRD, 'پایه سوم'),
    )
    level = models.CharField(max_length=1, choices=CHOICE_LEVEL)
    A, B = 'A', 'B'
    CHOICE_GROUP = (
        (A, 'کلاس الف'),
        (B, 'کلاس ب'),
    )
    group = models.CharField(max_length=1, choices=CHOICE_GROUP)
    HUMANITY, MATH, NATURAL = 'HU', 'MA', 'NA'
    CHOICE_FIELD = (
        (HUMANITY, 'علوم انسانی'),
        (MATH, 'علوم ریاضی'),
        (NATURAL, 'علوم تجربی'),
    )
    field = models.CharField(max_length=2, choices=CHOICE_FIELD)

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'

    def __str__(self):
        return self.get_field_display() + ' ' + self.get_level_display() + ' ' + self.get_group_display()


class Teacher(models.Model):
    teacher_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hire_date = models.DateField()
    DIPLOMA, ASSOCIATE, BACHELOR, MASTER, PHD = 'DI', 'FD', 'LI', 'FL', 'DR'
    CHOICE_DEGREE = (
        (ASSOCIATE, 'کاردانی'),
        (BACHELOR, 'لیسانس'),
        (MASTER, 'فوق لیسانس'),
        (PHD, 'دکتری'),
        (DIPLOMA, 'دیپلم'),
    )
    education_degree = models.CharField(max_length=2, choices=CHOICE_DEGREE)
    profession = models.ForeignKey('Course', on_delete=models.SET_NULL, null=True)
    classroom = models.ManyToManyField(Classroom)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'آموزگار'
        verbose_name_plural = 'آموزگاران'

    @property
    def experience(self):
        return datetime.now().year - self.hire_date.year


class Course(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'