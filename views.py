from django.shortcuts import render,redirect,HttpResponse
from Employee.models import Employee
from .forms import EmployeeForm

#creating the employees


def emp(request):
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass

    else:
        form=EmployeeForm()
    return render(request,'index.html',{'form':form})



#show(reading) the all employee

def show(request):
    employees=Employee.objects.all()
    return render(request,'show.html',{'employees':employees})



#edit the employee informations

def edit(request,id):
    employee=Employee.objects.get(id=id)
    return render(request,'edit.html',{'employee':employee})


#updating informations of employee posting

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'edit.html',{'employee':employee})

#deleting the record of employee

def destroy(request,id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')




