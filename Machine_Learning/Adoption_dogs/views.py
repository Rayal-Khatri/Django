from django.http import JsonResponse
import json

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def Adopt_Dogs(request):
    # Path to your JSON file
    json_file_path = 'C:\\Users\\user\\Desktop\\Repositories\\Django\Machine_Learning\\Dogs.json'  # Replace this with your JSON file path

    try:
        # Read the contents of the JSON file
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            print(data)
        return JsonResponse(data, safe=False)
    except FileNotFoundError:
        # Handle file not found error
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)