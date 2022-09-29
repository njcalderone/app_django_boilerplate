import os
from django.shortcuts import render
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Base_URL = config("SITE_BASE_URL")
KEYCLOAK_URL = config("KEYCLOAK_URL")
REALM_NAME = config("REALM_NAME")
ENCODED_REDIRECT_URI = config("ENCODED_REDIRECT_URI")


def login(request):
    return render(request, 'login.html', context={
        'base_url': Base_URL
    })


def redirect(request):
    return render(request, 'keycloakredirect.html')


def profile(request):
    return render(request, 'profile.html')

