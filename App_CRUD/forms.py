from django import forms
from django.forms import ModelForm
from .models import TOA

class TOAForm(ModelForm):
    class Meta:
        model = TOA
        
        fields = ('toa_name', 'toa_summary', 'toa_contact', 'toa_latitude', 'toa_longitude', 'image')

        widgets = {
            'toa_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'toa_summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Summary'}),
            'toa_contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact'}),
            'toa_latitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Latitude'}),
            'toa_longitude': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Longitude'}),
        }