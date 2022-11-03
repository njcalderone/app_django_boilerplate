import os
import django
import Project_Django_Boilerplate_GAP.views

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Django_Boilerplate_GAP.settings')
django.setup()

from App_Data_Table.models import Member2
from django.shortcuts import render, redirect
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Django_Boilerplate_GAP.settings')
django.setup()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Base_URL = config("SITE_BASE_URL")
KEYCLOAK_URL = config("KEYCLOAK_URL")
REALM_NAME = config("REALM_NAME")
ENCODED_REDIRECT_URI = config("ENCODED_REDIRECT_URI")


# Create your views here.
def index(request):
    all_members = Member2.objects.all()
    return render(request, 'datatables/index.html', {'all_members': all_members, 'base_url': Base_URL})


def insert(request):
    member = Member2(firstname=request.POST['firstname'], lastname=request.POST['lastname'],
                    eyecolor=request.POST['eyecolor'], height=request.POST['height'])
    member.save()
    return redirect(Base_URL + 'datatables/index.html')


from django.shortcuts import render
