from django.forms import ModelForm
from .models import Student
from django import forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ['id']


class TeacherSearchForm(forms.Form):
    first_name = forms.CharField(required=False, label='نام')
    last_name = forms.CharField(required=False, label='نام خانوادگی')
    hire_date = forms.DateTimeField(required=False, label='تاریخ استخدام', widget=forms.DateTimeInput(attrs={
        'class': 'form-control datetimepicker-input',
        'data-target': '#datetimepicker1'
    }))
