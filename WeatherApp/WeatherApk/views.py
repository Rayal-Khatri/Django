from django.shortcuts import render
import json
import urllib.request

def index(request):
    if request.method == 'POST':
        city= request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=53fbf5c1d2914764242cd964d811d1a5').read()
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon'])+ ' ' + str(json_data['coord']['lat']),
            "temp" : str(json_data['main']['temp'])+'K',
            "pressure": str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }

    else:
        data={}
    return render(request,'index.html',{'data':data,'city':city} )
# Create your views here.
#53fbf5c1d2914764242cd964d811d1a5