from django.forms import ModelForm
from django import forms
from a_post.models import *

from django.forms import ModelForm
from .models import Routes

class RouteForm(ModelForm):
    class Meta:
        model = Routes
        fields = ['name','email', 'contact']
        labels = {
            'name' : 'Enter Your Name',
            'email': 'Enter Your Email',
            'contact' : "Enter Your Messages",


        }
        widgets = {
            'contact': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a message ...', 'class': 'font1 text-4xl'}),
        }



class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        fields = ['url','body','tags']
        labels = {
            'body': 'Caption',
            'tags': 'Tags',

        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write Anything You want ', 'class': 'font2 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add a URl ...','class': 'font2 '}),
            'tags': forms.CheckboxSelectMultiple(),


        }

class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Tags',

        }
        widgets = {
            'body': forms.Textarea(attrs={'rows': 3,  'class': 'font1 text-4xl'}),
            'tags': forms.CheckboxSelectMultiple(),
        }


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        widgets= {
           'body' : forms.TextInput(attrs={'placeholder': 'Add Your Thoughts..'})
        }
        labels ={
           'body' : ''
        }


class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'add reply..', 'class': "!text-sm"})
        }

        labels = {
            'body' : ''
        }
class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = '__all__'

