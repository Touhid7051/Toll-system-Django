import django_filters
from django_filters import DateFilter

from .models import *

class DataFilter(django_filters.FilterSet):
    class Meta:
        model = Student_Admission
        fields ='__all__'
        exclude = ['student_image','created_at','updated_at', 'email']