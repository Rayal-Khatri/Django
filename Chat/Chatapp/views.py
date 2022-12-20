from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def chat(request):
    return render(request,'Room.html')