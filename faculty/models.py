from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class UserManager(BaseUserManager):
    def create_user(self, email, is_student=False, is_teacher=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            #date_of_birth=date_of_birth,
            is_student=is_student,
            is_teacher=is_teacher,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_student, is_teacher, password):
        user = self.create_user(
            email,
            password=password,
            #date_of_birth=date_of_birth,
            is_student=is_student,
            is_teacher=is_teacher,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )
    #date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_student', 'is_teacher']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Master(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Faculty(models.Model):
    masters = models.ManyToManyField(Master)
    name = models.CharField(max_length=50)
    capacity = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=50)
    #students = models.ManyToManyField(Student)
    masters = models.ManyToManyField(Master)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    #students = models.ManyToManyField(Student, blank=True)
    masters = models.ManyToManyField(Master)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    lessons = models.ManyToManyField(Lesson)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nation_code = models.IntegerField(unique=True, null=True, blank=True)
    age = models.IntegerField(default=18)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Class(models.Model):
    name = models.CharField(max_length=30)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    capacity = models.PositiveSmallIntegerField()
    lessons = models.ManyToManyField(Lesson)
    students = models.ManyToManyField(Student)
    OPEN = 'open'
    CLOSE = 'close'
    activate_choices = (
        (OPEN, 'open'),
        (CLOSE, 'close')
    )
    activate_field = models.CharField(default=OPEN, choices=activate_choices, max_length=250)

    def __str__(self):
        return self.name
