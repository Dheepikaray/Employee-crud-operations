from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

from emp_details.forms import EmpForm
from emp_details.models import Employee


# Create your views here.


def read(request):
    data = Employee.objects.all()
    return render(request, "index.html", {"data": data})


# delete-data
def delete(request, id):
    if request.method == 'POST':
        delt = Employee.objects.get(id=id)
        delt.delete()
        return redirect("read")
    return render(request, "index.html")

def add1(request):
    form = EmpForm()
    if request.method == "POST":
        form1 = EmpForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect("read")
        else:
            form=form1


    return render(request, "add.html", {"form": form})

def update(request,id):
    todo = Employee.objects.get(id=id)
    form = EmpForm(instance=todo)

    if request.method == 'POST':
        form1 = EmpForm(request.POST,instance=todo)
        if form1.is_valid():
            form1.save()
            return redirect("read")
        else:
            form=form1
    return render(request,'update.html',{'form':form})


