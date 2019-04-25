from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    courses = models.ManyToManyField("Course", through='StudentCourse', related_name='students')
    classrooms = models.ManyToManyField("Classroom", through='Register', related_name='students')
    last_modified_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Classroom(models.Model):
    A, B = 'A', 'B'
    CHOICE_GROUP = (
        (A, 'کلاس الف'),
        (B, 'کلاس ب'),
    )
    branch = models.CharField(max_length=1, choices=CHOICE_GROUP)
    level_field = models.ForeignKey("LevelField", on_delete=models.SET_NULL, null=True)
    education_year = models.CharField(max_length=20,null=True)
    courses = models.ManyToManyField('Course', through='TeacherClassCourse', related_name='classrooms')
    teachers = models.ManyToManyField('Teacher', through='TeacherClassCourse', related_name='classrooms')

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'

    def __str__(self):
        pass


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
    edu_degree = models.CharField(max_length=2, choices=CHOICE_DEGREE)
    profession = models.ManyToManyField('Course')
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
    unit = models.IntegerField(null=True)
    level_field = models.ForeignKey('LevelField', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'


class LevelField(models.Model):
    FIRST, SECOND, THIRD = '1', '2', '3',
    CHOICE_LEVEL = (
        (FIRST, 'پایه اول'),
        (SECOND, 'پایه دوم'),
        (THIRD, 'پایه سوم'),
    )
    level = models.CharField(max_length=1, choices=CHOICE_LEVEL)
    HUMANITY, MATH, NATURAL = 'HU', 'MA', 'NA'
    CHOICE_FIELD = (
        (HUMANITY, 'علوم انسانی'),
        (MATH, 'علوم ریاضی'),
        (NATURAL, 'علوم تجربی'),
    )
    field = models.CharField(max_length=2, choices=CHOICE_FIELD)


class StudentCourse(models.Model):
    student = models.ForeignKey('Student', related_name='student_courses', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', related_name='student_courses', on_delete=models.SET_NULL, null=True)
    final_grade = models.FloatField()
    mid_grade = models.FloatField()


class Register(models.Model):
    classroom = models.ForeignKey('Classroom', related_name='registers', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('Student', related_name='registers', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField()


class TeacherClassCourse(models.Model):
    teacher = models.ForeignKey('Teacher', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True)
    course = models.ForeignKey('Course', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey('Classroom', related_name='teacher_class_course', on_delete=models.SET_NULL,
                                  null=True)
    class_time = models.CharField(max_length=20)
