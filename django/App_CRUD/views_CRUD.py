from django.shortcuts import render, redirect
from .models import TOA
from .forms import TOAForm
from django.db.models import Q
from Project_Django_Boilerplate_GAP.views import get_user_roles


def toas_list(request):
    # toas = TOA.objects.all()

    search_query = ""

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    toas = TOA.objects.filter(
        Q(toa_name__icontains=search_query) | 
        Q(toa_contact__icontains=search_query) |
        Q(toa_summary__icontains=search_query)
    )
    roles = get_user_roles(request)
    if "Basic_User" in roles:
       access = "TRUE"
    else:
        access = "FALSE"
    context = {
        'toas': toas,
        'search_query': search_query,
        'login_roles': roles,
        'basic_access': access,
    }
    return render(request, 'toa/list.html', context)


def create_toa(request):
    form = TOAForm()

    if request.method == 'POST':
        form = TOAForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('toas-list')

    context = {
        'form': form,
    }
    return render(request, 'toa/create.html', context)


def edit_toa(request, pk):
    toa = TOA.objects.get(id=pk)
    form = TOAForm(instance=toa)

    if request.method == 'POST':
        form = TOAForm(request.POST, request.FILES, instance=toa)
        if form.is_valid():
            form.save()
            return redirect('toas-list')

    context = {
        'toa': toa,
        'form': form,
    }
    return render(request, 'toa/edit.html', context)


def delete_toa(request, pk):
    toa = TOA.objects.get(id=pk)

    if request.method == 'POST':
        toa.delete()
        return redirect('toas-list')

    context = {
        'toa': toa,
    }
    return render(request, 'toa/delete.html', context)
