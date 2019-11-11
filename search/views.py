from django.shortcuts import render
from chat.models import Post
from django.db.models import Q
from .models import SearchKeyword

# Create your views here.

def search(request):
    query = request.GET.get('q',"")
    results = keyword_results= []

    results = Post.objects.filter(Q(body__icontains = query) | Q(title__icontains = query))
    
    

    keyword_results = Post.objects.filter(
        searchkeyword__keyword__in =query.split()).distinct()
    
    
    result_num = results.count() + keyword_results.count()
    
    context = {
        "query":query,
        "results":results,
        "keyword_results":keyword_results,
        "result_num":result_num,
        }
    
    


    return render(request,"search/search_page.html",context)
   