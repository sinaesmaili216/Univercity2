from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import User
from .models import Lesson, Student, Master


class CreateStudent(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Student
        exclude = ['user']


class SelectLesson(forms.ModelForm):
    nation_code = forms.IntegerField()

    class Meta:
        model = Student
        fields = ['lessons']


class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class EditLessonsByMaster(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['lessons']


class RegisterMaster(forms.ModelForm):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Master
        exclude = ['user']


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'is_student', 'is_teacher')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password',
                  'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
