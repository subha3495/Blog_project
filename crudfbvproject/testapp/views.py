from django.shortcuts import render, redirect

from testapp.forms import EmployeeForm
from testapp.models import Employee
# Create your views here.

def list_view(request):
    employee = Employee.objects.all()
    return render(request,'testapp/list.html',{'employee':employee})

def create_view(request):
    form=EmployeeForm
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('home')

    return render(request,'testapp/create.html',{'form':form})

def delete_view(request,id):
    e=Employee.objects.get(id=id)
    e.delete()
    return redirect('home')

def update_view(request,id):
    employee=Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST,instance=employee)
        if form.is_valid:
            form.save()
            return redirect('home')
    return render(request,'testapp/update.html',{'employee':employee})