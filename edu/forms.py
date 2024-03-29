from django.forms import ModelForm, formset_factory
from .models import Student, Teacher, TeacherClassCourse, Course, Classroom, Register, User, StudentCourse, \
    StudentPresence, TeacherPresence
from django import forms
import jdatetime, datetime
from django.forms.models import inlineformset_factory


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TeacherClassCourseForm(ModelForm):
    class Meta:
        model = TeacherClassCourse
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TeacherClassCourseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TeacherForm(ModelForm):
    teacher_id = forms.IntegerField(label='کد پرسنلی')
    hire_date = forms.CharField(label='تاریخ استخدام', initial=datetime.date.today)
    profession = forms.ModelMultipleChoiceField(label='تخصص', queryset=(Course.objects.all()))
    edu_degree = forms.ChoiceField(label='مدرک تحصیلی', choices=Teacher.CHOICE_DEGREE)
    photo = forms.ImageField(label='تصویر پروفایل')
    father_name = forms.CharField(label='نام پدر')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_active']
        labels = {
            "username": "نام کاربری",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "is_active": "فعال",
            "email": "پست الکترونیک",
            "password": "کلمه عبور"
        }
        help_texts = {
            "username": "حداکثر ۱۵۰ کارکتر. استفاده از حروف، اعداد و کارکترهای @+-_ مجاز میباشد.",
            "is_active": "تصمیم بگیرید کاربر فعال باشد و یا خیر، بجای حذف کاربر از این گزینه استفاده نمایید.",
        }
        widgets = {
            'password': forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        pk = None
        if 'pk' in kwargs.keys():
            pk = kwargs.pop('pk')
        super(TeacherForm, self).__init__(*args, **kwargs)
        if pk is not None:
            teacher = Teacher.objects.get(pk=pk)
            jdata = jdatetime.date.fromgregorian(year=teacher.hire_date.year, month=teacher.hire_date.month,
                                                 day=teacher.hire_date.day)
            self.fields['teacher_id'].initial = teacher.teacher_id
            self.fields['hire_date'].initial = jdata.togregorian()
            self.fields['profession'].initial = teacher.profession.all()
            self.fields['edu_degree'].initial = teacher.edu_degree
            self.fields['photo'].initial = teacher.photo
            self.fields['father_name'].initial = teacher.father_name

        for visible in self.visible_fields():
            if visible.name is 'photo':
                visible.field.widget.attrs['class'] = 'form-control-file border'
            elif visible.name is 'hire_date':
                visible.field.widget.attrs['class'] = 'form-control datePicker'
            else:
                visible.field.widget.attrs['class'] = 'form-control'


class StudentForm(ModelForm):
    student_id = forms.IntegerField(label='شماره دانش آموزی')
    birthday = forms.CharField(label='تاریخ تولد')
    photo = forms.ImageField(label='تصویر پروفایل')
    education_field = forms.ChoiceField(choices=Student.CHOICE_education_field, label='رشته تحصیلی')
    father_name = forms.CharField(label='نام پدر')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email', 'is_active']
        labels = {
            "username": "نام کاربری",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "is_active": "فعال",
            "email": "پست الکترونیک",
            "password": "کلمه عبور"
        }
        help_texts = {
            "username": "حداکثر ۱۵۰ کارکتر. استفاده از حروف، اعداد و کارکترهای @+-_ مجاز میباشد.",
            "is_active": "تصمیم بگیرید کاربر فعال باشد و یا خیر، بجای حذف کاربر از این گزینه استفاده نمایید.",
        }
        widgets = {
            'password': forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        pk = None
        if 'pk' in kwargs.keys():
            pk = kwargs.pop('pk')
        super(StudentForm, self).__init__(*args, **kwargs)
        if pk is not None:
            student = Student.objects.get(pk=pk)
            jdata = jdatetime.date.fromgregorian(year=student.birthday.year, month=student.birthday.month,
                                                 day=student.birthday.day)
            self.fields['birthday'].initial = jdata.togregorian()
            self.fields['photo'].initial = student.photo
            self.fields['education_field'].initial = student.education_field
            self.fields['father_name'].initial = student.father_name
            self.fields['student_id'].initial = student.student_id

        for visible in self.visible_fields():
            if visible.name is 'photo':
                visible.field.widget.attrs['class'] = 'form-control-file border'
            elif visible.name is 'birthday':
                visible.field.widget.attrs['class'] = 'form-control datePicker'
            else:
                visible.field.widget.attrs['class'] = 'form-control'


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        exclude = ['courses', 'teachers']

    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class StudentSearchForm(forms.Form):
    student_id = forms.IntegerField(required=False, label='شماره دانش آموزی')
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')

    def __init__(self, *args, **kwargs):
        super(StudentSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class TeacherSearchForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')

    def __init__(self, *args, **kwargs):
        super(TeacherSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserSearchForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')
    user_name = forms.CharField(required=False, label='نام کاربری')

    def __init__(self, *args, **kwargs):
        super(UserSearchForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class RegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password', 'is_superuser', 'is_staff', 'email', 'is_active',
                  'groups', 'user_permissions']
        labels = {
            "username": "نام کاربری",
            "first_name": "نام",
            "last_name": "نام خانوادگی",
            "is_active": "فعال",
            "email": "پست الکترونیک",
            "password": "کلمه عبور",
            "groups": 'گروه ها',
            'user_permissions': 'دسترسی ها',
            'is_superuser': 'آیا کاربر مدیر سیستم می‌باشد؟',
            'is_staff': 'آیا کاربر از کارکنان می‌باشد؟',
        }
        help_texts = {
            "username": "حداکثر ۱۵۰ کارکتر. استفاده از حروف، اعداد و کارکترهای @+-_ مجاز می‌باشد.",
            "is_active": "تصمیم بگیرید کاربر فعال باشد و یا خیر، بجای حذف کاربر از این گزینه استفاده نمایید.",
            'is_superuser': 'انتخاب این گزینه تمامی دسترسی ها را به کاربر اعطا می‌کند',
            'is_staff': 'اجازه ورود در محیط ادمین را به کاربر می‌دهد.',
            "user_permissions": 'دسترسی های کاربر را مشخص می‌کند',
            'groups': 'گروه کاربر را مشخص می‌کند و تمامی دسترسی های لازم را به او می‌دهد'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name is 'is_superuser' or visible.name is 'is_staff' or visible.name is 'is_active':
                visible.field.widget.attrs['class'] = 'custom-control custom-checkbox'


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ["final_grade", 'mid_grade']


class StudentPresenceForm(forms.ModelForm):
    class Meta:
        model = StudentPresence
        fields = ['presence']


class TeacherPresenceForm(forms.ModelForm):
    class Meta:
        model = TeacherPresence
        fields = ['presence']


StudentPresenceFormset = formset_factory(StudentPresenceForm)
StudentCourseFormset = formset_factory(StudentCourseForm)
TeacherPresenceFormset = formset_factory(TeacherPresenceForm)
