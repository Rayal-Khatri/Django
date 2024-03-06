from django.http import HttpResponseNotFound, JsonResponse
from django.http import HttpResponse
import json
from django.conf import settings
import os

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def Adopt_Dogs(request):
    print("I was called")
    try:
        # Read the contents of the JSON file
        with open('C:\\Users\\user\\Desktop\\Repositories\\Django\Machine_Learning\\Dogs.json', 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Handle file not found error
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)
    

def Shelters(request):
    try:
        # Read the contents of the JSON file
        with open('C:\\Users\\user\\Desktop\\Repositories\\Django\Machine_Learning\\Shelters.json', 'r') as file:
            data = json.load(file)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Handle file not found error
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        # Handle other exceptions-
        return JsonResponse({'error': str(e)}, status=500)
    

def dog_image(request, dog_name):
    image_path = os.path.join(settings.STATIC_ROOT, 'Images/Dogs', f"{dog_name}")
    print(image_path)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type=f"Image")
    return HttpResponseNotFound()
            

def Shelter_image(request, Shelter_name):
    image_path = os.path.join(settings.STATIC_ROOT, 'Images/Shelters', f"{Shelter_name}")
    print(image_path)
    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type=f"Image")
    return HttpResponseNotFound()