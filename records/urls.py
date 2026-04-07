from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.add_course, name='add_course'),

    path('students/add/', views.add_student, name='add_student'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/edit/<int:pk>/', views.edit_student, name='edit_student'),
    path('students/delete/<int:pk>/', views.delete_student, name='delete_student'),

    path('marks/add/', views.add_mark, name='add_mark'),
]