from django.shortcuts import render, reverse
from django.utils.decorators import method_decorator

from .models import Student, Teacher, Classroom, TeacherClassCourse, Course, Register, StudentCourse, ClassTime, \
    StudentPresence
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.db.models import Q
from .forms import TeacherSearchForm, StudentSearchForm, StudentForm, UserSearchForm, TeacherForm, \
    TeacherClassCourseForm, CourseForm, ClassroomForm, RegisterForm, UserForm, StudentCourseForm
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test, login_required
import jdatetime

check_admin = user_passes_test(lambda u: Group.objects.get(name='admin') in u.groups.all())


@login_required
def index(request):
    return render(request, 'edu/index.html')


@method_decorator(check_admin, name='dispatch')
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
    form_class = UserForm

    # fields = '__all__'

    def get_success_url(self):
        return reverse('UserListView')


class UserEditView(UpdateView):
    model = User
    form_class = UserForm

    def get_success_url(self):
        return reverse('UserListView')


# Student Views
class StudentCreateView(CreateView):
    model = User
    form_class = StudentForm
    template_name = 'edu/student_form.html'

    def form_valid(self, form):
        student_data = {}
        for key in ('student_id', 'birthday', 'photo', 'father_name', 'education_field'):
            student_data[key] = form.cleaned_data.pop(key)
        datelist = student_data['birthday'].split('/')
        jdata = jdatetime.date(year=int(datelist[0]), month=int(datelist[1]), day=int(datelist[2]))
        student_data['birthday'] = jdata.togregorian()
        group = Group.objects.get(name='student')
        user = form.save()
        group.user_set.add(user)
        Student.objects.create(user=user, **student_data)
        return super().form_valid(form)

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

    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        student = Student.objects.get(pk=self.kwargs['pk'])
        birthday = context['student'].birthday
        context['student'].birthday = jdatetime.date.fromgregorian(year=birthday.year, month=birthday.month,
                                                                   day=birthday.day)
        if student.registers.first() is not None:
            classroom = student.registers.first().classroom
            teacher_class_courses = TeacherClassCourse.objects.filter(classroom=classroom)
            context.update({
                'teacher_class_courses': teacher_class_courses
            })
        return context


class StudentUpdateView(UpdateView):
    model = User
    form_class = StudentForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['pk'] = self.kwargs['pk']
        return kwargs

    def form_valid(self, form):
        student_data = {}
        for key in ('student_id', 'birthday', 'photo', 'father_name', 'education_field'):
            student_data[key] = form.cleaned_data.pop(key)
        datelist = student_data['birthday'].split('/')
        jdata = jdatetime.date(year=int(datelist[0]), month=int(datelist[1]), day=int(datelist[2]))
        student_data['birthday'] = jdata.togregorian()
        user = form.save()
        student = Student.objects.get(user=user)
        student.birthday = student_data['birthday']
        student.photo = student_data['photo']
        student.student_id = student_data['student_id']
        student.father_name = student_data['father_name']
        student.education_field = student_data['education_field']
        student.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('StudentListView')


#  Teacher class view

class TeacherCreateView(CreateView):
    model = User
    form_class = TeacherForm
    template_name = 'edu/teacher_form.html'

    def form_valid(self, form):
        teacher_date = {}
        for key in ('teacher_id', 'hire_date', 'edu_degree', 'profession', 'photo'):
            teacher_date[key] = form.cleaned_data.pop(key)
        user = form.save()
        Teacher.objects.create(user=user, **teacher_date)
        group = Group.objects.get(name='teacher')
        user = form.save()
        group.user_set.add(user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('TeacherListView')


class TeacherUpdateView(UpdateView):
    model = User
    form_class = TeacherForm

    def form_valid(self, form):
        teacher_date = {}
        for key in ('teacher_id', 'hire_date', 'edu_degree', 'profession', 'photo'):
            teacher_date[key] = form.cleaned_data.pop(key)
        user = form.save()
        Teacher.objects.create(user=user, **teacher_date)
        return super().form_valid(form)

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


# TeacherClassCourse CRUD
class TeacherClassCourseDetailView(DetailView):
    model = TeacherClassCourse


class TeacherClassCourseCreateView(CreateView):
    model = TeacherClassCourse
    form_class = TeacherClassCourseForm

    def get_success_url(self):
        return reverse('TeacherClassCourseList')


class TeacherClassCourseListView(ListView):
    model = TeacherClassCourse


class TeacherClassCourseUpdateView(UpdateView):
    model = TeacherClassCourse
    form_class = TeacherClassCourseForm

    def get_success_url(self):
        return reverse('TeacherClassCourseList')


# Course CRUD
class CourseCreate(CreateView):
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse('CourseList')


class CourseUpdate(UpdateView):
    model = Course
    form_class = CourseForm

    def get_success_url(self):
        return reverse('CourseList')


class CourseList(ListView):
    model = Course


class CourseDetail(DetailView):
    model = Course


# Classroom CRUD
class ClassroomCreate(CreateView):
    model = Classroom
    form_class = ClassroomForm

    def get_success_url(self):
        return reverse('ClassroomList')


class ClassroomUpdate(UpdateView):
    model = Classroom
    form_class = ClassroomForm

    def get_success_url(self):
        return reverse('ClassroomList')


class ClassroomList(ListView):
    model = Classroom


class ClassroomStudentDetail(DetailView):
    model = Classroom
    template_name = 'edu/classroomstudent_detail.html'


class ClassroomCourseDetail(DetailView):
    model = Classroom
    template_name = 'edu/classroomcourse_detail.html'


class ClassroomStudentList(DetailView):
    model = Classroom


class RegisterUpdate(UpdateView):
    model = Register

    def get_success_url(self):
        return reverse('RegisterList')


class RegisterCreate(CreateView):
    model = Register
    form_class = RegisterForm

    def form_valid(self, form):
        for course in form.cleaned_data['classroom'].courses.all():
            student = form.cleaned_data['student']
            StudentCourse.objects.get_or_create(course=course, student=student)
        return super(RegisterCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse('RegisterList')


class RegisterDetail(DetailView):
    model = Register


class RegisterList(ListView):
    model = Register


class StudentCourseListView(ListView):
    model = StudentCourse

    def get_queryset(self):
        pk = self.kwargs['pk']
        queryset = super().get_queryset()
        tcc = TeacherClassCourse.objects.get(pk=pk)
        queryset = queryset.filter(student__registers__classroom=tcc.classroom, course=tcc.course)
        return queryset


def error_404_view(request, exception):
    return render(request, '404.html')


class StudentPresenceList(ListView):
    model = StudentPresence
