from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.
class Student(models.Model):
    student_id = models.IntegerField(verbose_name='شماره دانش آموزی')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری', primary_key=True,
                                related_name='student')
    courses = models.ManyToManyField("Course", through='StudentCourse', related_name='students',
                                     verbose_name='دورس ')
    classrooms = models.ManyToManyField("Classroom", through='Register', related_name='students',
                                        verbose_name='کلاس ها')
    last_modified_date = models.DateTimeField(verbose_name='تاریخ آخرین ویرایش', auto_now_add=True)
    photo = models.ImageField(upload_to='student_profiles', null=True, blank=True)

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name


class Teacher(models.Model):
    teacher_id = models.IntegerField(verbose_name='کد پرسنلی')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری', primary_key=True,
                                related_name='teacher')
    hire_date = models.DateField(verbose_name='تاریخ استخدام')
    DIPLOMA, ASSOCIATE, BACHELOR, MASTER, PHD = 'DI', 'FD', 'LI', 'FL', 'DR'
    CHOICE_DEGREE = (
        (ASSOCIATE, 'کاردانی'),
        (BACHELOR, 'لیسانس'),
        (MASTER, 'فوق لیسانس'),
        (PHD, 'دکتری'),
        (DIPLOMA, 'دیپلم'),
    )
    edu_degree = models.CharField(max_length=2, choices=CHOICE_DEGREE, verbose_name='مدرک تحصیلی')
    profession = models.ManyToManyField('Course', verbose_name='تخصص')
    photo = models.ImageField(upload_to='teacher_profiles', null=True, blank=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    class Meta:
        verbose_name = 'آموزگار'
        verbose_name_plural = 'آموزگاران'

    @property
    def experience(self):
        return datetime.now().year - self.hire_date.year


class LevelField(models.Model):
    FIRST, SECOND, THIRD = '1', '2', '3',
    CHOICE_LEVEL = (
        (FIRST, 'پایه اول'),
        (SECOND, 'پایه دوم'),
        (THIRD, 'پایه سوم'),
    )
    level = models.CharField(max_length=1, choices=CHOICE_LEVEL, verbose_name='پایه تحصیلی')
    HUMANITY, MATH, NATURAL = 'HU', 'MA', 'NA'
    CHOICE_FIELD = (
        (HUMANITY, 'علوم انسانی'),
        (MATH, 'علوم ریاضی'),
        (NATURAL, 'علوم تجربی'),
    )
    field = models.CharField(max_length=2, choices=CHOICE_FIELD, verbose_name='رشته تحصیلی')

    class Meta:
        verbose_name = 'لیست پایه های تحصیلی'
        verbose_name_plural = 'لیست پایه های تحصیلی'

    def __str__(self):
        return self.get_level_display() + " " + self.get_field_display()


class Classroom(models.Model):
    A, B = 'A', 'B'
    CHOICE_GROUP = (
        (A, 'کلاس الف'),
        (B, 'کلاس ب'),
    )
    branch = models.CharField(max_length=1, choices=CHOICE_GROUP, verbose_name='شماره کلاس')
    level_field = models.ForeignKey("LevelField", on_delete=models.SET_NULL, null=True, verbose_name='مقطع تحصیلی')
    education_year = models.CharField(max_length=20, null=True, verbose_name='سال تحصیلی')
    courses = models.ManyToManyField('Course', through='TeacherClassCourse', related_name='classrooms',
                                     verbose_name='دروس')
    teachers = models.ManyToManyField('Teacher', through='TeacherClassCourse', related_name='classrooms',
                                      verbose_name='اساتید')

    class Meta:
        verbose_name = 'کلاس'
        verbose_name_plural = 'کلاس ها'

    def __str__(self):
        return str(self.level_field) + " " + self.get_branch_display()


class Course(models.Model):
    name = models.CharField(max_length=20, verbose_name='نام درس')
    unit = models.IntegerField(null=True, verbose_name='تعداد واحد')
    level_field = models.ForeignKey('LevelField', on_delete=models.SET_NULL, null=True, verbose_name='مقطع تحصیلی')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درس'
        verbose_name_plural = 'دروس'


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
    teacher = models.ForeignKey('Teacher', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True,
                                verbose_name='نام استاد')
    course = models.ForeignKey('Course', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True,
                               verbose_name='نام درس')
    classroom = models.ForeignKey('Classroom', related_name='teacher_class_course', on_delete=models.SET_NULL,
                                  null=True, verbose_name='پایه تحصیلی')
    class_time = models.CharField(max_length=20, verbose_name='زمان کلاس')
