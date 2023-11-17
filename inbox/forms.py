from django import forms
from django.forms import ModelForm
from .models import Inbox

class InboxMessageForm(ModelForm):
    class Meta:
        model = Inbox
        fields = ['body']
        labels ={
            'body' : ''
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows' : 4 , 'placeholder': 'add message ..'}),
        }