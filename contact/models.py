from django.db import models
from django import forms

# Create your models here.

class Contact(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=250)
    message = forms.CharField(widget=forms.Textarea)