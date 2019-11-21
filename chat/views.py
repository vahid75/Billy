from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,TemplateView,UpdateView,DeleteView,CreateView,DetailView 
from django.core.mail import send_mail
from .models import *
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from .forms import Search_Form
from django.utils import timezone




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


# from django.views.generic.edit import FormView
#for handling the forms with a "form.py" file and class based "FormView" view.

# class contact(FormView):            # a class based view for form handling
#     template_name = 'chat/names.html'
#     success_url = '/thanks'
#     form_class = ContactForm

#     def form_valid(self,form):      # 'form' argument is reqiered in this method
        
#         #add functions
#         return super().form_valid(form) 
                
# ------------------------------------------------------------------#

class Postlist(ListView):
    
    model = Post
    form_class = "Search_form"
    template_name = 'chat/home.html'
    context_object_name = 'posts'   

    """return every user's post in home page. """

    def get_queryset(self):
        username = self.request.user              
        return User.objects.get(username = username).post_set.all()
    
    
# ------------------------------------------------------------------#
      

class Postcreate(LoginRequiredMixin,CreateView):
    form_class = Create_Post_Form
    template_name = 'chat/Postcreate.html'  
    def class_name(self):
        name  = "Create your post here"
        return name



    
    # template_name_suffix = '_tt'                 #by prepering this, the template that uses is 'Model name +_tt.html'.by default this view use 'post_form.html'       
   
    """first return the form object by set commmit to false to set the post's author to the username that filled the form."""     
    def form_valid(self,form):
        formy = form.save(commit = False)
        # formy.author = settings.AUTH_USER_MODEL.objects   .get(username = request.user.username)
        formy.author = self.request.user
        formy.save()
        return super().form_valid(form)       
      
        
# ------------------------------------------------------------------#


class Postupdate(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = Update_Post_Form
    template_name = 'chat/Postcreate.html'         
    
    # success_url = reverse_lazy('chat:home')
    def class_name(self):
        name  = "Update your post here"
        return name

    # def get_queryset(self):
    #     return Post.objects.get(pk= self.id)




class Postdetail(DetailView):

    model = Post
    template_name = 'chat/postdetail.html'
    context_object_name = 'e'   
    # slug_field = "slug"
    
    """overriding the get_object method to set the user's last accessed time to the post object.  """
    def get_object(self):
        obj = super().get_object()
        # Record the last accessed date
        obj.last_accessed = timezone.now()
        obj.save()
        return obj
   
    # def get_object(self):
    #     obj = get_object_or_404(
    #         self.model,
    #         slug = self.kwargs['slug'],
    #         # creation_date__year = self.kwargs['year'],
    #         creation_date__month = self.kwargs['month'],
    #         creation_date__day = self.kwargs['day'],
            
    #         )
    #     return obj  



    


class Postdelete(DeleteView):
    model = Post
    # template_name = 'chat/confiramtion.html'
    success_url = reverse_lazy('chat:home')
   
    
    def get(self, request, **kwargs):
        return self.post(request, **kwargs)
    
      

# def someview(request):
    
#     e = Post.objects.all()    
#     x=str(request.get_host()) 
#     response = HttpResponse(x)
#     response.write("<p>Here's the text of the Web page.</p>")
#     return response

        
    
    




# class Comment_Create(CreateView):
#     form_class = Create_Comment_Form  
#     template_name = 'chat/comments.html' 
   
#     def get_context_data(self,**kwargs):
#         context = super().get_context_data(**kwargs)
#         context["comment"] = context["form"]
#         return context

    # def form_valid(self,form):
    #     formy = form.save(commit=False)
    #     formy.post = Postdetail.get_object() 
    #     formy.save()
    #     return super().form_valid(form)