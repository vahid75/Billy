from django.contrib import admin
from .models import *
from search.models import PostAdmin

# Register your models here.
admin.site.register(Post,PostAdmin)
# admin.site.register(Comments)
