from django.shortcuts import render
from django.http import JsonResponse
import subprocess
from django.http import JsonResponse
from Machine_Learning.Symptom_Analysis.Neural_Network import predict_diseases

def predict_api(request):
    if request.method == 'POST':
        test_data = request.POST.getlist('test_data[]')
        results = predict_diseases(test_data)
        return JsonResponse(results, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'})
def home(request):
    return render(request, 'home.html')

