from django.db import models
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class TOA(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    toa_name = models.CharField(max_length=200)
    toa_summary = models.CharField(max_length=1000)
    toa_contact = models.CharField(max_length=200)
    toa_latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)],)
    toa_longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)],)
    
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.toa_name

    @property
    def imageURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        
        return url