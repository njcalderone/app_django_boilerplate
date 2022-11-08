import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Project_Django_Boilerplate_GAP.settings')
from django.db import models


# Create your models here.
class Member(models.Model):
    objects = None
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    eyecolor = models.CharField(max_length=50)
    height = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname, " ", self.lastname
