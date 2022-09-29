import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Django_Boilerplate_GAP.settings')
django.setup()
from django.db import models


# Create your models here.
class Member(models.Model):
    objects = None
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname, " ", self.lastname
