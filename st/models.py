from django.db import models

# Create your models here.

class Student(models.Model):

    name = models.CharField(max_length=64)
    sername = models.CharField(max_length=64)
    faculty = models.CharField(max_length=64)
    group = models.CharField(max_length=64)
    program = models.CharField(max_length=64)
    year = models.DateField()
    photo = models.ImageField()
    study_starting_time = models.TimeField()
    study_end_time = models.TimeField()


    def __str__(self):
        return self.name


class Project(models.Model):

    title = models.CharField(max_length=64)
    start_time = models.DateField()
    fimish_time = models.DateField()
    student = models.ManyToManyField(Student, null = True, blank = True, default = '-')


    def __str__(self):
        return self.title
