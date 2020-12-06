from django.contrib import admin


# Register your models here.
from CRUD_App.models import Student_Admission , User_Profile

admin.site.register(Student_Admission)
admin.site.register(User_Profile)