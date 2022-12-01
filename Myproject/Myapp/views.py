from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # contex={
    #     'name':'Rayal',
    #     'age' :21,                is used to send data as object to the HTML file
    #     'nationality' : "Nepali"
    # }
  # # name = 'Rayal'
    return render(request,'index.html')
# Create your views here.

def counter(request):
    text=request.GET['text']
    no_of_words = len(text.split())
    return render(request,'count.html',{'words' : no_of_words})
