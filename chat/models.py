from django.db import models
from django.utils import timezone
# from django.forms import ModelForm,TextInput,PasswordInput
from django import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings
from django.contrib import admin
from taggit.managers import TaggableManager
from markdown import markdown
from django.utils.text import slugify




# Create your models here.




class Post_published_Manager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status = self.model.PUBLISHED)




    


class Post(models.Model):  


    DRAFT = "DRF"
    PUBLISHED = "PUB"
    BAN = "BAN"  

    status_choices =[
        (DRAFT,"draft"),
        (PUBLISHED,"publised"),
        (BAN,"ban"),
        ]

    
    title = models.CharField(max_length=100)    
    creation_date  = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    slug = models.SlugField(unique_for_date="creation_date",null=True,blank = True)
    commments_alow = models.BooleanField(default=True)
    tags = TaggableManager(blank=True) 
    body = models.TextField(null = True,blank = True)
    excerpt = models.TextField(max_length=100,blank =True)
    body_html = models.TextField(null = True,blank = True)
    excerpt_html = models.TextField(blank = True,null= True,editable = False)
    last_accessed = models.DateTimeField(null =True,blank = True)
    status = models.CharField(max_length = 3,choices = status_choices,default = DRAFT)

    objects = models.Manager()
    publish = Post_published_Manager()
   
   
    

    
    
    def get_absolute_url(self):
        return reverse('chat:details',
        kwargs = {
            'slug':self.slug,
            'year':self.creation_date.year,       
            'month':self.creation_date.month,
            'day':self.creation_date.day,            
            }
            )

    def __str__(self):
        return self.title   

    # def publish(self):
    #     self.creation_date =timezone.now()
    #     self.save() 

    def save(self,*args,**kwargs):
        if self.body:
            self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)



class PosttAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title")}
    
    
    

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

        error_messages = {
            'username':{
                'unique':"the username or password is incorrect",
            }
           
        }
       
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'user','id':'',"placeholder":"Username"}),
            'password': forms.PasswordInput(attrs={'class': 'pass','id':'',"placeholder":"Password"}),
            'email': forms.EmailInput(attrs={'class': 'user','id':'',"placeholder":"Email"}),

        }


# class post_form(models.ModelForm):
#     class Meta:
#         model = Post
#         widgets = {
#            "author":
#         }


class Create_Post_Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['title','body','tags','excerpt','status','commments_alow']
        
        widgets = {
        'title': forms.TextInput(attrs={'class': 'form-control','id':'validationCustom01',"placeholder":"Just 100 character"}),
        'body': forms.Textarea(attrs={'class': 'form-control','id':'validationCustom03',"placeholder":"Body"}),
        'tags': forms.TextInput(attrs={'class': 'form-control','id':'validationCustom02',"placeholder":"Tags"}),
        'excerpt': forms.Textarea(attrs={'class': 'form-control','id':'validationCustom04',"placeholder":"Post excerpt here"}),
        'status': forms.Select(attrs={'class': 'form-control','id':'validationCustom04',"placeholder":"Post excerpt here"}),
        
        }


class Update_Post_Form(Create_Post_Form):
    pass

        