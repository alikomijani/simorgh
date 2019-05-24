from django.forms import ModelForm
from .models import Student, Teacher, TeacherClassCourse
from django import forms


class TeacherClassCourseForm(ModelForm):
    class Meta:
        model = TeacherClassCourse
        fields = "__all__"


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['courses', 'classrooms']


class StudentSearchForm(forms.Form):
    student_id = forms.IntegerField(required=False, label='شماره دانش آموزی')
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')


class TeacherSearchForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')
    # hire_date = forms.DateTimeField(required=False, label='تاریخ استخدام', widget=forms.DateTimeInput(attrs={
    #     'class': 'form-control datetimepicker-input',
    #     'data-target': '#datetimepicker1'
    # }))


class UserSearchForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')
    user_name = forms.CharField(required=False, label='نام کاربری')
