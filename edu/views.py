from django.shortcuts import render
from .models import Student, Teacher, Course, Classroom
from django.views.generic.edit import FormView
from .forms import StudentForm


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
