from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from json import JSONEncoder, loads
import requests
from .models import Student, Teacher, Course, Classroom


# Create your views here.

def get_class_students(request, class_id):
    classroom = Classroom.objects.filter(id=class_id).first()
    teacher = Teacher.objects.filter(classroom=classroom).first()
    student_list = list(Student.objects.filter(classroom=classroom))
    return render(request, 'edu/class_list.html',
                  {'teacher': teacher, 'student_list': student_list, 'classroom': classroom})
