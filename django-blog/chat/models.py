from django.db import models
from django.utils import timezone
# from django.forms import ModelForm,TextInput,PasswordInput
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


# Create your models here.


class Post(models.Model):    
    title = models.TextField(max_length=100)
    context = models.TextField(max_length=255)
    creation_date  = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    # creation_date  = models.DateTimeField(blank = True,null = True)

    


    def get_absolute_url(self):
        return reverse('chat:details',kwargs = {'pk':self.pk})

    def __str__(self):
        return self.title   

    # def publish(self):
    #     self.creation_date =timezone.now()
    #     self.save() 


class Comment(models.Model):
    author = models.CharField(max_length=255)
    comment_con = models.TextField(max_length=255)    
    creation_date  = models.DateTimeField(default = timezone.now)
    post = models.ForeignKey(Post,on_delete= models.CASCADE)
    
    def __str__(self):
        return self.author


    
# class Authorform(forms.ModelForm):
#     class Meta:
#         model  = Post
#         fields = ['author','title','context','creation_date']
        
#         # widgets = {
#         #     'title': forms.Textarea(attrs={"class":'red'})
#         # }   

#     def __init__(self):
#         super().__init__()
#         self.fields['author'].widget.attrs.update({'class': 'special'})





class Userinfo(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","email"]

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control','id':'inputEmail3',"placeholder":"Username"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control','id':'inputPassword3',"placeholder":"Password"}),
            'email': forms.EmailInput(attrs={'class': 'form-control','id':'inputEmail3',"placeholder":"Email"}),

        }


# class post_form(models.ModelForm):
#     class Meta:
#         model = Post
#         widgets = {
#            "author":
#         }
