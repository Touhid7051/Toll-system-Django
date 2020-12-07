from django.urls import path
from .views import student_admission, index, student_list, Student_details, student_update, Student_delete, \
    registerPage, loginPage , logutPage ,search

from django.contrib.auth import views as auth_views #for changing password

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

    #For reset password

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_sent.html'),name="password_reset_done"),

path(
    'reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_form.html'),name='password_reset_confirm',),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_done.html'),name="password_reset_complete"),

]