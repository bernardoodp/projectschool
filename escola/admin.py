from django.contrib import admin
from escola.models import Student, Course


class Students(admin.ModelAdmin):
    list_display = ('id', 'name', 'rg', 'cpf', 'born_date')
    list_display_links = ('id', 'name')
    search_fields = ['name']
    list_per_page = 20

admin.site.register(Student, Students)

class Courses(admin.ModelAdmin):
    list_display = ('id', 'code_course', 'description')
    list_display_links = ('id', 'code_course')
    search_fields = ['code_course']

admin.site.register(Course, Courses)


# Register your models here.
