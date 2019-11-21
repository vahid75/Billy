from django.db import models
from chat.models import Post
from django.contrib import admin

# Create your models here.

class SearchKeyword(models.Model):
    keyword = models.CharField(max_length=50)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

    def __str__(self):
        return self.keyword


class SearchKeywordInline(admin.StackedInline):
    model = SearchKeyword
    
    

"""
This model is a psudo base model that 'inline' model would edit in its admin page.
It means both models in on single page.
The included one named 'inline'. 

"""
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    inlines=[
        SearchKeywordInline,
    ]

  