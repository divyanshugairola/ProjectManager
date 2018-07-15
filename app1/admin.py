from django.contrib import admin
from app1.models import Head,Department,Employee,Project,Submission
# Register your models here.
admin.site.register(Head)
admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Submission)