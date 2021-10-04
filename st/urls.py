from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('students/', views.students, name = 'students'),
    path('students/projects/<int:project_id>/', views.projects, name = 'projects'),
]
