from django.contrib import admin
from .models import Classroom, Teacher, Student, Course, Register, LevelField, StudentCourse, ClassTime, \
    TeacherClassCourse

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Register)
admin.site.register(Teacher)
admin.site.register(LevelField)
admin.site.register(StudentCourse)
admin.site.register(ClassTime)
admin.site.register(TeacherClassCourse)
