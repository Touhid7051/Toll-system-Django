from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from django.shortcuts import render,redirect

# Create your views here.
from CRUD_App.decorators import unauthenticated_user , allowed_users
from CRUD_App.forms import Student_Admission_from, CreateUserForm
from CRUD_App.models import Student_Admission

from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from .filters import DataFilter



@login_required(login_url = 'login')
def index(request):
    return render(request,'index.html')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def student_admission(request):
    form = Student_Admission_from(request.POST , request.FILES)
    data = Student_Admission.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('index')
    context = {'form' : form , 'data': data}





    return render(request,'student_admission_data.html', context)


@login_required(login_url = 'login')
def student_list(request):

    data=Student_Admission.objects.all()
    myFilter = DataFilter(request.GET, queryset=data)  # Filter Functionalities
    data = myFilter.qs
    context={'data' : data , 'myFilter' : myFilter }
    return render(request, 'student_list.html',context)


@login_required(login_url = 'login')
def Student_details(request, id):
    data = Student_Admission.objects.get(id = id)
    context = {'data' : data }
    return render(request, 'student_details.html', context)



@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def student_update(request, id):
    data =Student_Admission.objects.get(id=id)

    form = Student_Admission_from(request.POST, request.FILES , instance=data)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('student_list')
    context = {'form': form}
    return render(request, 'student_admission_data.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def Student_delete(request,id):
    data = Student_Admission.objects.get(id=id)
    data.delete()
    return redirect('student_list')

@unauthenticated_user
def registerPage(request):
    #if request.user.is_authenticated:
     #   return redirect('index')

    #else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                user=form.save()
                username =form.cleaned_data.get('username')

                group = Group.objects.get(name = 'customer')
                user.groups.add(group)

                messages.success(request, 'Account is created for ' +  username )
                return redirect('login')

        context = {'form' : form}
        return render(request, 'register.html' , context )



@unauthenticated_user
def loginPage(request):
    #if request.user.is_authenticated:
        #return redirect('index')

    #else:
        if request.method == 'POST' :
           username = request.POST.get('username')
           password = request.POST.get('password')
           user = authenticate(request ,username = username ,password = password)

           if user is not None:
               login(request , user)
               return redirect('index')

           else:
               messages.info(request, 'Username or Password is incorrect')
        context ={}
        return render(request, 'login.html', context)


def logutPage(request):
    logout(request)
    return redirect('login')



