

from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.http import HttpResponse
from .forms import  Emp_new
from .models import *


# Create your views here.
def index(request):
    return render(request,'ProjectManagement/index.html')

def add(request,id=0):
    if request.method == 'GET':
        if id==0:
            form=Emp_new()
            return render(request,'ProjectManagement/addData.html',{'form':form})
        else:
            employee=Employees_new.objects.get(pk=id)
            form=Emp_new(instance=employee)
            return render(request,'ProjectManagement/addData.html',{'form':form})
    else:
        if id==0:
            args = {
                'Employee_name': request.POST['Employee_name'],
                'Employee_id': request.POST['Employee_id'],
                'Employee_contact': request.POST['Employee_contact'],
                'emp_status': 'Pending',
                'project_id': request.POST['project_id'],
            }

            form=Emp_new(args)
            if form.is_valid():
                form.save()
            return redirect('Emp_show')
        else:
            employee=Employees_new.objects.get(pk=id)
            form=Emp_new(request.POST,instance=employee)
            if form.is_valid():
                form.save()
            return redirect('Emp_show')

def show(request):
    if request.method=="GET":
        employee_list=Employees_new.objects.all().order_by('Employee_name')
    else:
        employee_list = Employees_new.objects.filter(Employee_name__startswith = request.POST['text'])
    return render(request,'ProjectManagement/show.html',{'employee_list':employee_list})


def delete(request,id):
    employee=Employees_new.objects.get(pk=id)
    employee.delete()
    return redirect("Emp_show")

def showProject(request):
    if request.method == 'POST':
        print("POSTING")
        emp_list = Employees_new.objects.filter(project_id=request.POST['project'])
        projects_list = Projects.objects.all()
        return render(request, 'ProjectManagement/showProject.html', context={'projects':projects_list, 'employee_list':emp_list})
    else:
        projects_list = Projects.objects.all()
        return render(request, 'ProjectManagement/showProject.html', context={'projects':projects_list})


#######################                       EMPLOYEEE SECTION          ####################################

def empView(request):
    emps=Employees_new.objects.all()
    args={
        'emps':emps
    }
    return render(request,'ProjectManagement/employeeview.html',args)


def empPortal(request, id):

    if request.method == 'POST':
        emp=Employees_new.objects.get(pk=id)
        emp.emp_status = request.POST['status_field']
        emp.save()


    emp=Employees_new.objects.get(pk=id)
    args={
        'emp':emp
    }
    return render(request,'ProjectManagement/employeeportal.html',args)



