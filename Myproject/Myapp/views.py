from django.shortcuts import render
from django.http import HttpResponse
from . models import People 
def index(request):
    person1 = People()
    person1.name ="Subodh Dahal"
    person1.comment =" This is a super useful website"

    person2 = People()
    person2.name ="Barsha Rai"
    person2.comment =" The UI is super simple to use"
    
    person3 = People()
    person3.name ="Rizen Shakya"
    person3.comment =" I dont even read book but i use this Website"
    
    person4 = People()
    person4.name ="Sujal Maharjan"
    person4.comment =" I am super dum and only thing smart i do is use this site"
    
    persons =[person1,person2,person3,person4]
    return render(request,'index.html',{'persons':persons})

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
