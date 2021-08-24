from django.shortcuts import render,redirect
from testapp.models import Employee
from testapp.forms import EmployeeForms
# Create your views here.

def list_view(request):
    Employees = Employee.objects.all()
    return render(request,'testapp/index.html',{'Employees':Employees})

def create_view(request):
    form = EmployeeForms()
    if request.method == 'POST':
        form = EmployeeForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    return render(request,'testapp/create.html',{'form':form})
def delete_view(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('home')

def update_view(request,id):
    employee = Employee.objects.get(id=id)
    if request.method=='POST':
        form=EmployeeForms(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'testapp/update.html',{'employee':employee})

