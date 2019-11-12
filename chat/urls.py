"""URLCONF FILE

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.urls import re_path,include,path
from chat.views import *
from django.contrib.auth import urls
from django.contrib.auth import views as auth_views



app_name = 'chat'
urlpatterns = [  
    
    path('home/',Postlist.as_view(),name= 'home'),
    path('form/',Postcreate.as_view(),name = 'create'),
    path('details/<year>/<month>/<day>/<slug:slug>/',Postdetail.as_view(), name= 'details'),
    path('update/<int:pk>',Postupdate.as_view(),name= 'postupdate'),  
    path('delete/<int:pk>',Postdelete.as_view(),name = 'deletepost'),
    path('accounts/',include('django.contrib.auth.urls')), 
    # path('logout/',
    #     auth_views.LogoutView.as_view(next_page = reverse_lazy('chat:home')),name = 'logout'),
          
    path("accounts/password_change",auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy("chat:password_change_done")
    ),name="password_change"),   
     
    path('notfound/',someview),
    path("register/",register,name="reg"),    
    path("logout/",logoutnlogin,name = "logout"),
    



]