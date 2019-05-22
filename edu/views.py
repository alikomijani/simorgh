from django.shortcuts import render, redirect
from .models import Student, Teacher, Classroom
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.db.models import Q
from .forms import TeacherSearchForm , StudentForm
from rest_framework import viewsets
from .serializers import StudentSerializer
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required(login_url='/login/')
def index(request):
    return render(request, 'edu/index.html')


# Create your views here.
def get_student_rest_api(request, pk):
    student = Student.objects.filter(student_id=pk)
    serial = StudentSerializer(student, many=True)
    return JsonResponse(serial.data, safe=False)


def get_all_student_rest_api(request):
    student = Student.objects.all()
    serial = StudentSerializer(student, many=True)
    print(JsonResponse(serial.data, safe=False).serialize())
    return JsonResponse(serial.data, safe=False)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


def get_class_students(request, class_id):
    classroom = Classroom.objects.filter(id=class_id).first()
    teacher = Teacher.objects.filter(classroom=classroom).first()
    student_list = list(Student.objects.filter(classroom=classroom))
    return render(request, 'edu/class_list.html',
                  {'teacher': teacher, 'student_list': student_list, 'classroom': classroom})


class StudentCreateView(CreateView):
    model = Student
    fields = ['student_id', 'user', 'photo']
    success_url = '../list'
    def form_valid(self, form):
        form.instance.last_modified_date = self.request.user
        return super(StudentCreateView, self).form_valid(form)


class UserListView(ListView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = '__all__'
    success_url = '../list'


class StudentListView(ListView):
    model = Student
    form_class = StudentForm
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(student_id=query)
        else:
            return Student.objects.all()

class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['student_id', 'user', 'last_modified_date']
    success_url = '../list'


#  Teacher class view

class TeacherCreateView(CreateView):
    model = Teacher
    fields = ['teacher_id', 'hire_date', 'user', 'edu_degree', 'profession', 'photo']
    success_url = '../list'


class TeacherListView(ListView):
    # context_object_name = 'teachers'
    model = Teacher
    form_class = TeacherSearchForm

    def get_context_data(self, **kwargs):
        context = super(TeacherListView, self).get_context_data(**kwargs)
        context.update({
            'search': self.form_class()
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')
        if self.request.GET and any([first_name, last_name]):
            queryset = queryset.filter(
                Q(user__first_name=first_name) | Q(user__last_name=last_name))
        return queryset


class TeacherDetailView(DetailView):
    model = Teacher


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['teacher_id', 'user', 'hire_date', 'edu_degree', 'profession']
    success_url = '../list'
