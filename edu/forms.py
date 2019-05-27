from django.forms import ModelForm
from .models import Student, Teacher, TeacherClassCourse, Course, Classroom, Register,User
from django import forms


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
    first_name= forms.CharField(label='نام')
    last_name =forms.CharField(label='نام خانوادگی')
    user_name=forms.CharField(label='نام کاربری')
    email =forms.CharField(label='ایمیل')
    password =forms.CharField(label='کلمه عبور')
    class Meta:
        model = Teacher
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        exclude = ['courses', 'teachers']

    def __init__(self, *args, **kwargs):
        super(ClassroomForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class StudentForm(ModelForm):
    student_id = forms.IntegerField(label='شماره دانش آموزی')
    birthday = forms.DateField(label='تاریخ تولد')
    photo = forms.ImageField(label='تصویر پروفایل')
    class Meta:
        model = User
        fields = ['username','first_name','last_name','is_active','email','password']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
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

    # hire_date = forms.DateTimeField(required=False, label='تاریخ استخدام', widget=forms.DateTimeInput(attrs={
    #     'class': 'form-control datetimepicker-input',
    #     'data-target': '#datetimepicker1'
    # }))
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
