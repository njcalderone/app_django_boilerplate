from django import template
from django.shortcuts import render
import requests
import json
from keycloak import KeycloakOpenID
from decouple import config
register = template.Library()

