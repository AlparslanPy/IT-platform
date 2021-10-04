# Generated by Django 3.2 on 2021-09-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('st', '0006_students_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='courses',
        ),
        migrations.RemoveField(
            model_name='students',
            name='course',
        ),
        migrations.RemoveField(
            model_name='students',
            name='project',
        ),
        migrations.AddField(
            model_name='students',
            name='project',
            field=models.ManyToManyField(blank=True, default='-', null=True, to='st.Project'),
        ),
    ]