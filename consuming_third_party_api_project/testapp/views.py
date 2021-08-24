from django.shortcuts import render
import requests
# Create your views here.
def get_geographic_info(request):
    ip=request.META.get('HTTP_X_FORWARDED_FOR',"") or request.META.get('REMOTE_ADDR')
    # url='http://api.ipstack.com/'+str(ip)+'?access_key=80edf8cfe41574ce95d881e9c9957369'
    url='http://api.ipstack.com/157.41.125.139?access_key=80edf8cfe41574ce95d881e9c9957369'
    response = requests.get(url)
    data = response.json()
    return render(request,'testapp/info.html',data)