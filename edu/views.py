from django.shortcuts import render
from .models import Student, Teacher, Course, Classroom
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView


# Create your views here.

def get_class_students(request, class_id):
    classroom = Classroom.objects.filter(id=class_id).first()
    teacher = Teacher.objects.filter(classroom=classroom).first()
    student_list = list(Student.objects.filter(classroom=classroom))
    return render(request, 'edu/class_list.html',
                  {'teacher': teacher, 'student_list': student_list, 'classroom': classroom})


class StudentCreateView(CreateView):
    model = Student
    fields = ['student_id', 'user', 'last_modified_date']
    success_url = '../../list'


class StudentListView(ListView):
    model = Student


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['student_id', 'user', 'last_modified_date']
    success_url = '../../list'


#  Teacher class view

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['teacher_id', 'hire_date', 'user', 'edu_degree', 'profession']
    success_url = '../../list'


class TeacherListView(ListView):
    model = Teacher


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['teacher_id', 'user', 'hire_date', 'edu_degree', 'profession']
    success_url = '../../list'
