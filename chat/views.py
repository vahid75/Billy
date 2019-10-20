from django.shortcuts import render
from django.views.generic import ListView,TemplateView,UpdateView,DeleteView,CreateView,DetailView #for form handling with "modelform" and class based views.

from django.http import(HttpResponse,
                        HttpResponseRedirect,
                        Http404,
                        HttpResponseNotFound,
                        HttpRequest,
                        # from .forms import * 
                        )

from django.core.mail import send_mail
from .models import *
from django.urls import reverse,reverse_lazy
from django.views.generic.edit import FormView   #for handling the forms with a "form.py" file and class based "FormView" view.

from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.conf import settings








# Create your views here.




# def formy(request):
    
#     if request.method == 'POST':
#         initialy= {
#             'yourname': 'put your title'
#         }
#         form = ContactForm(request.POST,initial=initialy)


#         if form.is_valid():
#             author = form.cleaned_data['author']
#             title =form.cleaned_data['title']
#             context = form.cleaned_data['context']
#             creation_date = form.cleaned_data['creation_date']
#             form.save()
#             return HttpResponseRedirect('thanks/')

#     else:
#         i=  {
#             'yourname': 'put wr title'
#         }
#         form = ContactForm(initial={'yourname': 'put your title'})
#         form = ContactForm(initial=i)
#     # content = {
#     #     'form' : form
#     # }
    
#     return render(request,'chat/ty.html', {
#         'form' : form
#     })





# ------------------------------------------------------------------#


# class contact(FormView):            # a class based view for form handling
#     template_name = 'chat/names.html'
#     success_url = '/thanks'
#     form_class = ContactForm

#     def form_valid(self,form):      # 'form' argument is reqiered in this method
        
#         #add functions
#         return super().form_valid(form) 


    
                


# ------------------------------------------------------------------#


# def notfound(request):
#     return render(request,'chat/404.html')

# ------------------------------------------------------------------#

class Postlist(LoginRequiredMixin,ListView):
    
    model = Post
    template_name = 'chat/home.html'
    context_object_name = 'posts'   
    

    def get_queryset(self):
        username = self.request.user.username        
        return User.objects.get(username = username).post_set.all()
    
    
# ------------------------------------------------------------------#
      

class Postcreate(LoginRequiredMixin,CreateView):
    model= Post
    template_name = 'chat/Postcreate.html'         #specifing a template name
    # template_name_suffix = '_tt'                 #by prepering this, the template that uses is 'Model name +_tt.html'.by default this view use 'post_form.html'                    
    fields = ['title','context','creation_date']

    def form_valid(self,form):
        formy = form.save(commit = False)
        # formy.author = settings.AUTH_USER_MODEL.objects   .get(username = request.user.username)
        formy.author = self.request.user
        formy.save()
        return super().form_valid(form)         

    
    
        
# ------------------------------------------------------------------#dummmmmmy titlle
# dummmmmmy text from anybody


class Postupdate(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = 'chat/Postcreate.html'         
    fields = ['title','context','creation_date']
    success_url = reverse_lazy('chat:home')

    # def get_queryset(self):
    #     return Post.objects.get(pk= self.id)




class Postdetail(DetailView):

    model = Post
    template_name = 'chat/postdetail.html'
    context_object_name = 'e'


    


class Postdelete(DeleteView):
    model = Post
    # template_name = 'chat/confiramtion.html'
    success_url = reverse_lazy('chat:home')
   
    
    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
      


# from django.contrib.auth.models import User
# user = User.objects.create_user('johny', 'lennony@thebeatles.com', 'johnypassword')

def someview(request):
    
    e = Post.objects.all()
    
    x=str(request.get_host()) 
    response = HttpResponse(x)
    response.write("<p>Here's the text of the Web page.</p>")
    return response

        
    
    
def register(request):
    if request.method == "POST":
        userinfoo = Userinfo(request.POST)        
        if userinfoo.is_valid():
            # username  =userinfoo.cleaned_data["username"]           
            # email = userinfoo.cleaned_data["email"]
            user = userinfoo.save(commit=False)            
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse("chat:home"))


    else:
        userinfoo = Userinfo()
    
    return render(request,"chat/register.html",{"userinfoo":userinfoo})


def authenticating(request):
    
    if request.method == "POST":
        
        userinfoo = Userinfo(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        authed_user = authenticate(request , username = username , password = password)

        if authed_user is not None: 
            login(request,authed_user)
            print("you are login as {}". format(username))            
            return HttpResponseRedirect(reverse("chat:home"))

        else:
            if User.objects.get(username = "{}".format(username)) is not None : 
                context = {
                    "userinfoo":userinfoo,
                    "in_pass":"password is incorrect",
                }
                return render(request,"chat/home.html",context)
                 
            else:

                return HttpResponse("there is no {} account on this website".format(username)) 
            

    else:        
        userinfoo = Userinfo()
        context = {
            "userinfoo":userinfoo,
            

        }
    # return render(request,"chat/authenticate.html",context)
    return render(request,"chat/login.html",context)




# def logout_then_login(request):
#     return super().logout_then_login()

def logoutnlogin(request):
    """
    Logout n login back
    """
    return logout_then_login(request,login_url = reverse('chat:auth'))