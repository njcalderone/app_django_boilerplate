from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Q
from Project_Django_Boilerplate_GAP.views import get_user_roles


def employees_list(request):
    # employees = Employee.objects.all()

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    employees = Employee.objects.filter(
        Q(emp_name__icontains=search_query) | 
        Q(emp_role__icontains=search_query) |
        Q(emp_salary__icontains=search_query)
    )
    roles = get_user_roles(request)
    if "Basic_User" in roles:
       access = "TRUE"
    else:
        access = "FALSE"
    context = {
        'employees': employees,
        'search_query': search_query,
        'login_roles': roles,
        'basic_access': access,
    }
    return render(request, 'employee/list.html', context)


def create_employee(request):
    form = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'form': form,
    }
    return render(request, 'employee/create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('employees-list')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'employee/edit.html', context)


def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('employees-list')

    context = {
        'employee': employee,
    }
    return render(request, 'employee/delete.html', context)
