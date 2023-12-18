from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .Neural_Network import train_model, predict_top_3_diseases
import json

# Train the model when the server starts
# train_model()

@csrf_exempt
def predict_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        test_data = data.get('test_data', [])
        results = predict_top_3_diseases(test_data)
        return JsonResponse(results, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method.'})

def home(request):
    if request.method == 'POST':
        symptoms = request.POST.getlist('symptoms[]')
        results = predict_top_3_diseases(symptoms)
        print(results)
        return JsonResponse(results, safe=False)

    return render(request, 'home.html')

