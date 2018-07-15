from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length = 15) 

    def __str__(self):
        return self.name


class Head(models.Model):
    user=models.OneToOneField(User,
                                on_delete=models.CASCADE)
    department=models.ForeignKey(Department,
                                on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.user.username

class Employee(models.Model):
    user=models.OneToOneField(User,
                                on_delete=models.CASCADE)
    head = models.ForeignKey(Head,
                                on_delete=models.CASCADE,blank=True)
    def __str__(self):
        return self.user.username

class Project(models.Model):
    project_name=models.CharField(max_length=20)
    project_head=models.ForeignKey(Head,
                                        on_delete=models.CASCADE)
    project_desc=models.TextField(blank=True)
    subm_date=models.DateField(default=datetime.now(),blank=True)


    def __str__(self):
        return self.project_name

class Submission(models.Model):
    p_id=models.ForeignKey(Project,
                                    on_delete=models.CASCADE)
    e_id=models.ForeignKey(Employee,
                                    on_delete=models.CASCADE,blank=True)
    date_of_submission =models.DateTimeField(auto_now_add=True)
    # sub_file = 

    # def __str__(self):
    #     return self.Project.p_id





