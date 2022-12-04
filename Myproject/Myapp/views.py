from django.shortcuts import render
from django.http import HttpResponse
from . models import Features 
def index(request):
    features = Features.objects.all()
    return render(request,'index.html',{'persons':features})

def counter(request):
    name = request.POST['name']
    message = request.POST['message']
    return render(request,'responce.html',{'name':name,'msg':message})
# def counter(request):
#     text=request.POST['text']          #Post is for private data  
#     no_of_words = len(text.split())
#     context={
#         'words' : no_of_words,
#         'content' : text
#     }
#     return render(request,'count.html',context)
