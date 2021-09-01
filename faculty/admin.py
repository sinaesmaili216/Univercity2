from django.contrib import admin
from .models import Faculty, Course, Lesson, Master, Student, Class
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin', 'is_student', 'is_teacher')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_student', 'is_teacher')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ['name', 'capacity']
    filter_horizontal = ['masters']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    filter_horizontal = ['masters']


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['course', 'name']


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['faculty', 'first_name', 'last_name']


def change_to_close(modeladmin, request, queryset):
    queryset.update(activate_field='close')


change_to_close.short_description = 'change_to_close'


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ['name', 'faculty', 'capacity', 'activate_field']
    filter_horizontal = ['lessons', 'students']
    actions = [change_to_close]
