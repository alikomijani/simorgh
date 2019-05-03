from django.shortcuts import render
from .models import Student, Teacher, Course, Classroom
from django.views.generic.edit import FormView
from .forms import StudentForm
from django.views.generic import ListView
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import UpdateView


# Create your views here.

def get_class_students(request, class_id):
    classroom = Classroom.objects.filter(id=class_id).first()
    teacher = Teacher.objects.filter(classroom=classroom).first()
    student_list = list(Student.objects.filter(classroom=classroom))
    return render(request, 'edu/class_list.html',
                  {'teacher': teacher, 'student_list': student_list, 'classroom': classroom})


class FormRegisterStudent(FormView):
    template_name = 'edu/register.html'
    form_class = StudentForm
    success_url = '/edu/register/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class StudentListView(ListView):
    model = Student


    def get_context_data(self, **kwargs):
        context = super(StudentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class StudentDetailView(DetailView):
    model = Student


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['student_id']
