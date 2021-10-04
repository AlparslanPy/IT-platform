from django.db import models

# Create your models here.
class Project(models.Model):

    title = models.CharField(max_length=64)
    start_time = models.DateField()
    fimish_time = models.DateField()

    def __str__(self):
        return self.title


class Students(models.Model):

    name = models.CharField(max_length=64)
    sername = models.CharField(max_length=64)
    faculty = models.CharField(max_length=64)
    group = models.CharField(max_length=64)
    program = models.CharField(max_length=64)
    project = models.ManyToManyField(Project,null = True, blank = True, default = '-')


    def __str__(self):
        return self.name
