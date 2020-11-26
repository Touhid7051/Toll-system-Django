from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect

# Create your views here.
from CRUD_App.forms import Student_Admission_from, CreateUserForm
from CRUD_App.models import Student_Admission

from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout



@login_required(login_url = 'login')
def index(request):
    return render(request,'index.html')

@login_required(login_url = 'login')
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
    context={'data' : data}
    return render(request, 'student_list.html',context)


@login_required(login_url = 'login')
def Student_details(request, id):

    data = Student_Admission.objects.get(id = id)
    context = {'data' : data}
    return render(request, 'student_details.html', context)



@login_required(login_url = 'login')
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
def Student_delete(request,id):
    data = Student_Admission.objects.get(id=id)
    data.delete()
    return redirect('student_list')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                form.save()
                user =form.cleaned_data.get('username')
                messages.success(request, 'Account is created for ' +  user )
                return redirect('login')

        context = {'form' : form}
        return render(request, 'register.html' , context )


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')

    else:
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



