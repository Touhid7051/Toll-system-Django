from django.db import models

# Create your models here.

class Student_Admission(models.Model):
    name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=200)
    mother_name = models.CharField(max_length=200)
    number = models.IntegerField(max_length=11)
    email = models.EmailField(max_length=200)
    student_image = models.ImageField(upload_to="Student_Admission")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    def image_url(self):
        if self.student_image:
            return self.student_image.url
        else:
            return ""

