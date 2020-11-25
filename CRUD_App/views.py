from django.shortcuts import render,redirect

# Create your views here.
from CRUD_App.forms import Student_Admission_from
from CRUD_App.models import Student_Admission


def index(request):
    return render(request,'index.html')

def student_admission(request):
    form = Student_Admission_from(request.POST , request.FILES)
    data = Student_Admission.objects.all()
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('index')
    context = {'form' : form , 'data': data}





    return render(request,'student_admission_data.html', context)


def student_list(request):

    data=Student_Admission.objects.all()
    context={'data' : data}
    return render(request, 'student_list.html',context)

def Student_details(request, id):

    data = Student_Admission.objects.get(id = id)
    context = {'data' : data}
    return render(request, 'student_details.html', context)


def student_update(request, id):
    data =Student_Admission.objects.get(id=id)

    form = Student_Admission_from(request.POST, request.FILES , instance=data)
    if form.is_valid():
        form = form.save(commit=False)
        form.save()
        return redirect('student_list')
    context = {'form': form}
    return render(request, 'student_admission_data.html', context)

def Student_delete(request,id):
    data = Student_Admission.objects.get(id=id)
    data.delete()
    return redirect('student_list')

