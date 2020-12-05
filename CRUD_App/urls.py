from django.urls import path
from .views import student_admission, index, student_list, Student_details, student_update, Student_delete, \
    registerPage, loginPage , logutPage ,search

urlpatterns = [
    path('', index ,name='index'),
    path('admission_form/', student_admission ,name='student_admission'),
    path('student_list/', student_list ,name='student_list'),
    path('student_details/<int:id>/', Student_details ,name='student_details'),
    path('student_update/<int:id>/', student_update, name='student_update'),
    path('student_delete/<int:id>/', Student_delete, name='Student_delete'),
    path('register/', registerPage , name='register'),
    path('login/', loginPage , name='login'),
    path('logout/', logutPage , name='logout'),
    path('search/', search, name='search'),

]