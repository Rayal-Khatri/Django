from django.http import HttpResponseNotFound, JsonResponse
from django.http import HttpResponse
import json
from django.conf import settings
import os

from django.shortcuts import render

json_file_path = 'C:\\Users\\user\\Desktop\\Repositories\\Django\Machine_Learning\\Dogs.json'  # Replace this with your JSON file path
def home(request):
    return render(request, 'home.html')

def Adopt_Dogs(request):
    try:
        # Read the contents of the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            print("I was called")
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Handle file not found error
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)
    

def dog_image(request, dog_name):
    image_extensions = ['.jpg', '.png', '.webp']  # List of supported image file extensions

    for extension in image_extensions:
        image_path = os.path.join(settings.STATIC_ROOT, 'Images\\Dogs', f"{dog_name}{extension}")
        if os.path.exists(image_path):
            with open(image_path, 'rb') as f:
                return HttpResponse(f.read(), content_type=f"image/{extension[1:]}")

    return HttpResponseNotFound()