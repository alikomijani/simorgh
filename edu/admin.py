from django.contrib import admin
from .models import Classroom, Teacher, Student, Course

# Register your models here.
admin.site.register(Classroom)
admin.site.register(Course)
admin.site.register(Student)


class Teacheradmin(admin.ModelAdmin):
    list_display = ('user', 'hire_date', 'experience', 'education_degree', 'profession', 'teacher_id')
    list_display_links = ('user', 'hire_date', 'experience', 'education_degree', 'profession', 'teacher_id')
    list_filter = ('user',)
    fields = ('user', 'hire_date')
    empty_value_display = 'None'
    search_fields = ('user__username', 'education', 'hire_date')
    ordering = ['hire_date', 'user']
    # readonly_fields = ['user']


admin.site.register(Teacher, Teacheradmin)
