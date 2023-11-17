from django.forms import ModelForm
from django import forms
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        labels = {
            'real_name' : 'Name'
        }
        widgets = {
            'image': forms.FileInput(),
            'bio': forms.Textarea(attrs={'rows': 2})
        }
