from django.urls import path
from .views import show_class_list, class_info, create_student, select_lesson, index, login_user, \
    search_in_class_list, students_list, edit_student_lessons_by_master, register_master, logout_user

app_name = 'faculty'
urlpatterns = [
    path('index', index, name='index'),
    path('class_list/', show_class_list, name='class_list'),
    path('class_info/<name>/', class_info, name='class_info'),
    path('create_student/', create_student, name='create_student'),
    path('select_lesson', select_lesson, name='select_lesson'),
    path('login', login_user, name='login'),
    path('logout', logout_user, name='logout'),
    path('search', search_in_class_list, name='search'),
    path('students_list', students_list, name='students_ist'),
    path('edit_lessons_by_master/<student_name>', edit_student_lessons_by_master, name='edit_student_lessons_by_master'),
    path('register_master', register_master, name='register_master')
]

