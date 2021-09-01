from django.urls import path
from .views import show_class_list, show_students_and_lessons, create_student, select_lesson, index, login_user, \
    search_in_class_list, students_list, edit_student_lessons_by_master, register_master

app_name = 'faculty'
urlpatterns = [

    path('class_list/', show_class_list, name='class_list'),
    path('student_and_lesson/<name>/', show_students_and_lessons, name='student_and_lesson'),
    path('create_student/', create_student, name='create_student'),
    path('select_lesson', select_lesson, name='select_lesson'),
    path('login', login_user, name='login'),
    path('search', search_in_class_list, name='search'),
    path('students_list', students_list, name='students_ist'),
    path('edit_lessons_by_master/<student_name>', edit_student_lessons_by_master, name='edit_student_lessons_by_master'),
    path('register_master', register_master, name='register_master')
]

