from django.contrib import admin

# Register your models here.
from .models import Project, Student

admin.site.register(Project)
admin.site.register(Student)
