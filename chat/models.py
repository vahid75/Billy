from django.db import models
from django import forms
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager
from django.utils import timezone  
from markdown import markdown
from django.utils.text import slugify       


# Create your models here.



# This class belongs to custom 'Post' model manager and returns objects that their 'status' is 'Published'.
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
    
    #At first we should declare the original model maneger that is "objects" by default
    objects = models.Manager()
    # Then instantiated the custom manager to connect the model to its manager
    publish = Post_published_Manager()
   
   
    # cause the 'detail' view url captures the year,slug,month and day , we should declare the 'kwargs' argument to definite these parts in url
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
    
    
    """ 
    To save the marked down texts in 'body_html' field, we override the 'save' method to convert raw text to markdown text (in this case HTML).

    Every time that we override the save method ,we should confident that we pass '*args' and '**kwargs' arguments in the function defenition and super object. it ensure that this method captured its own arguments and every posibillity that may added to this method in future .
    """ 
    
    def save(self,*args,**kwargs):
        if self.body:
            self.body_html = markdown(self.body)
        if self.excerpt:
            self.excerpt_html = markdown(self.excerpt)
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)


from django.contrib import admin
class PosttAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title")}





# -------------------ModelForms is written here--------------------#

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

        'commments_alow': forms.CheckboxInput(attrs={'class': 'custom-control-input','id':'customSwitch1'}),
        
        }


# cause this form functionality is the same as Create_Post_Form we subclass it to reduce summerize code
class Update_Post_Form(Create_Post_Form):
    pass



