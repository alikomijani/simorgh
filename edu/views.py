from django.shortcuts import render, redirect
from .models import Student, Teacher, Classroom, TeacherClassCourse
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import UpdateView
from django.views.generic import CreateView
from django.db.models import Q
from .forms import TeacherSearchForm, StudentSearchForm, StudentForm, UserSearchForm, TeacherForm, \
    TeacherClassCourseForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


@login_required(login_url='/login/')
def index(request):
    return render(request, 'edu/index.html')


def get_class_students(request, class_id):
    classroom = Classroom.objects.filter(id=class_id).first()
    teacher = Teacher.objects.filter(classroom=classroom).first()
    student_list = list(Student.objects.filter(classroom=classroom))
    return render(request, 'edu/class_list.html',
                  {'teacher': teacher, 'student_list': student_list, 'classroom': classroom})


class UserListView(ListView):
    model = User
    form_class = UserSearchForm

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context.update({
            'search': self.form_class
        })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        first_name = self.request.GET.get('first_name')
        last_name = self.request.GET.get('last_name')
        if self.request.GET and any([first_name, last_name]):
            queryset = queryset.filter(
                Q(first_name__icontains=first_name) & Q(last_name__icontains=last_name))
        return queryset


class UserDetailView(DetailView):
    model = User


class UserCreateView(CreateView):
    model = User
    fields = '__all__'

    def get_success_url(self):
        return reverse('UserListView')


class UserEditView(UpdateView):
    model = User
    fields = '__all__'

    def get_success_url(self):
        return reverse('UserListView')


# Student Views
class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('StudentListView')


class StudentListView(ListView):
    model = Student
    form_class = StudentSearchForm

    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
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
                Q(user__first_name__icontains=first_name) & Q(user__last_name__icontains=last_name))
        return queryset


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return reverse('StudentListView')


#  Teacher class view

class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm

    def get_success_url(self):
        return reverse('TeacherListView')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm

    def get_success_url(self):
        return reverse('TeacherListView')


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
                Q(user__first_name__icontains=first_name) & Q(user__last_name__icontains=last_name))
        return queryset


class TeacherDetailView(DetailView):
    model = Teacher


# TeacherClassCourse
class TeacherClassCourseDetailView(DetailView):
    model = TeacherClassCourse


class TeacherClassCourseCreateView(CreateView):
    model = TeacherClassCourse
    form_class = TeacherClassCourseForm

    def get_success_url(self):
        return reverse('TeacherClassCourseListView')


class TeacherClassCourseListView(ListView):
    model = TeacherClassCourse


class TeacherClassCourseUpdateView(UpdateView):
    model = TeacherClassCourse
    form_class = TeacherClassCourseForm

    def get_success_url(self):
        return reverse('TeacherClassCourseList')
