from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Features 
from . models import Namesofpeople 

def index(request):
    features = Features.objects.all()
    Namesofpep = Namesofpeople.objects.all()
    return render(request,'index.html',{'persons':features,'names':Namesofpep})

def counter(request):
    name = request.POST['name']
    message = request.POST['message']
    return render(request,'responce.html',{'name':name,'msg':message})

def register(request):
    if request.method =="POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pw']
        password2 = request.POST['pw2']

        if password==password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request,'Username already in use')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'Password Incorrect!')
            return redirect('register')
    else:
        return render(request,'register.html' )


def login(request):
    return render(request,'login.html')

# def counter(request):
#     text=request.POST['text']          #Post is for private data  
#     no_of_words = len(text.split())
#     context={
#         'words' : no_of_words,
#         'content' : text
#     }
#     return render(request,'count.html',context)
