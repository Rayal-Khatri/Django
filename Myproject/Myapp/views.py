from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    contex={
        'name':'Rayal',
        'age' :21,
        'nationality' : "Nepali"
    }
    # name = 'Rayal'
    return render(request,'index.html',contex)
# Create your views here.
