from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Neural_Network import predict_diseases
import json

@csrf_exempt
def predict_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        test_data = data.get('test_data', [])
        print(test_data)
        results = predict_diseases(test_data)
        return JsonResponse(results, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'})


def home(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms[]')
        results = predict_diseases(symptoms)
        print(results)
        return JsonResponse(results, safe=False)

    return render(request, 'home.html')
