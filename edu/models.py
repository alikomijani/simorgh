from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
import jdatetime


# Create your models here.

# abstract person
class Person(models.Model):
    birthday = models.DateField(verbose_name='تاریخ تولد', blank=True, null=True)
    last_modified_date = models.DateTimeField(verbose_name='تاریخ آخرین ویرایش', auto_now_add=True, blank=True,
                                              null=True)
    photo = models.ImageField(upload_to='profiles', null=True, blank=True, verbose_name='تصویر پروفایل')
    father_name = models.CharField(max_length=40, verbose_name='نام پدر', blank=True, null=True)

    class Meta:
        abstract = True


class Student(Person, models.Model):
    student_id = models.IntegerField(verbose_name='شماره دانش آموزی')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری', primary_key=True,
                                related_name='student')
    courses = models.ManyToManyField("Course", through='StudentCourse', related_name='students',
                                     verbose_name='دورس ')
    classrooms = models.ManyToManyField("Classroom", through='Register', related_name='students',
                                        verbose_name='کلاس ها')
    math, humanities, experimental = 'MA', 'HU', 'EX'
    CHOICE_education_field = (
        (math, 'ریاضی و فیزیک'),
        (humanities, 'علوم انسانی'),
        (experimental, 'علوم تجربی')
    )

    education_field = models.CharField(max_length=2, choices=CHOICE_education_field, verbose_name='رشته تحصیلی',
                                       blank=True, null=True)

    class Meta:
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name


class Teacher(Person, models.Model):
    teacher_id = models.IntegerField(verbose_name='کد پرسنلی')
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='نام کاربری', primary_key=True,
                                related_name='teacher')
    hire_date = models.DateField(verbose_name='تاریخ استخدام')
    DIPLOMA, ASSOCIATE, BACHELOR, MASTER, PHD = 'DI', 'FD', 'LI', 'FL', 'DR'
    CHOICE_DEGREE = (
        (ASSOCIATE, 'کاردانی'),
        (BACHELOR, 'کارشناسی'),
        (MASTER, 'کارشناسی ارشد'),
        (PHD, 'دکتری'),
        (DIPLOMA, 'دیپلم'),
    )
    edu_degree = models.CharField(max_length=2, choices=CHOICE_DEGREE, verbose_name='مدرک تحصیلی')
    profession = models.ManyToManyField('Course', verbose_name='تخصص')

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
    student = models.ForeignKey('Student', related_name='student_courses', on_delete=models.SET_NULL, null=True,
                                blank=True)
    course = models.ForeignKey('Course', related_name='student_courses', on_delete=models.SET_NULL, null=True,
                               blank=True)
    final_grade = models.FloatField(null=True, blank=True)
    mid_grade = models.FloatField(null=True, blank=True)


class Register(models.Model):
    classroom = models.ForeignKey('Classroom', related_name='registers', on_delete=models.SET_NULL, null=True)
    student = models.ForeignKey('Student', related_name='registers', on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name='فعال', help_text='برای غیرفعال کردن کلاس از این گزینه استفاده کنید',default=True)


class TeacherClassCourse(models.Model):
    teacher = models.ForeignKey('Teacher', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True,
                                verbose_name='نام استاد')
    course = models.ForeignKey('Course', related_name='teacher_class_course', on_delete=models.SET_NULL, null=True,
                               verbose_name='نام درس')
    classroom = models.ForeignKey('Classroom', related_name='teacher_class_course', on_delete=models.SET_NULL,
                                  null=True, verbose_name='پایه تحصیلی')
    class_times = models.ManyToManyField('ClassTime', related_name='teacher_class_course', verbose_name='زمان کلاس')
    is_active = models.BooleanField(verbose_name='فعال', help_text='برای غیرفعال کردن کلاس از این گزینه استفاده کنید',
                                    default=True)


class ClassTime(models.Model):
    MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY = 'MO', 'TU', 'WE', 'TH', 'FR', 'SA', 'SU'
    CHOICE_DAY = (
        (SATURDAY, 'شنبه'),
        (SUNDAY, 'یکشنبه'),
        (MONDAY, 'دوشنبه'),
        (TUESDAY, 'سه شنبه'),
        (WEDNESDAY, 'چهارشنبه'),
        (THURSDAY, 'پنجشنبه'),
        (FRIDAY, 'جمعه'),
    )
    class_day = models.CharField(max_length=2, choices=CHOICE_DAY, verbose_name='روز کلاس', blank=True, null=True)
    FIRST, SECOND, THIRD, FORTH= 'FI', 'SE', 'TH', 'FO'
    CHOICE_TIME = (
        (FIRST, 'زنگ اول'),
        (SECOND, 'زنگ دوم'),
        (THIRD, 'زنگ سوم'),
        (FORTH, 'زنگ چهارم'),
    )
    class_time = models.CharField(max_length=2, choices=CHOICE_TIME, verbose_name='زنگ', blank=True, null=True)

    def __str__(self):
        return self.get_class_day_display() + ' ' + self.get_class_time_display()
    @property
    def time(self):
        return self.get_class_time_display()
    @property
    def day(self):
        return self.get_class_day_display()

class StudentPresence(models.Model):
    student_course = models.ForeignKey('StudentCourse', on_delete=models.CASCADE)
    presence = models.BooleanField(verbose_name='حاضر')
    data = models.DateField('تاریخ')
    class_time = models.ForeignKey('ClassTime', on_delete=models.SET_NULL, null=True)
