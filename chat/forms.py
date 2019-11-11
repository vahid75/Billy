from django import forms
from .models import *



class ContactForm(forms.Form):
    yourname = forms.CharField(label="put your name hear:",max_length=30)
    subject = forms.CharField(label="subject:",max_length=40)
    message = forms.CharField(label="message:",widget=forms.Textarea)
    to = forms.EmailField(label="to:")
    recipients = ['info@example.com']

class themeform(forms.Form):
    name = forms.CharField(label= 'name field:',max_length=100)
    
class Search_Form(forms.Form):
    search_box = forms.CharField(max_length=30)

