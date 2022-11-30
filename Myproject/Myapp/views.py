from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>Hey!This is my first Django Website</h1>')

# Create your views here.
