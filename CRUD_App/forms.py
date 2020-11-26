from .models import Student_Admission
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Student_Admission_from(ModelForm):

    class Meta:
        model = Student_Admission
        fields = ['name','father_name','mother_name','email','number','student_image']



class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username' , 'email' , 'password1' , 'password2']