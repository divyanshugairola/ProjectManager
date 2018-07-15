from django import forms
from django.contrib.auth.models import User
from app1.models import Head,Employee,Project

class UserForm(forms.ModelForm):
    password= forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class HeadForm(forms.ModelForm):
    class Meta():
        model=Head
        fields=('department',)

class EmployeeForm(forms.ModelForm):
    class Meta():
        model=Employee
        fields=('head',)


class ProjectForm(forms.ModelForm):
    class Meta():
        model=Project
        fields=('project_name','project_head','project_desc','subm_date')


