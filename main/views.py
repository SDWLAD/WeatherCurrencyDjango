from . import *
from django.shortcuts import render, HttpResponse
from .weather import *

def index(request): return render(request, 'index.html')
def about(request): return render(request, 'about.html')

def translator(request): 
    if request.method == "POST":
        return render(request, "translator.html", context={"input":request.POST['input'], 'output':translate(request)})
    return render(request, "translator.html")

def weather(request):
    try: city = requests.get(f"http://ip-api.com/json/{get_client_ip(request)}?lang=uk").json()['city']
    except: city = "Polonne"
    if request.method == 'POST': city = request.POST['city']
    will_weather = [week[((int(today.strftime("%w"))+i)%7)-1] for i in range(5)]
    return render(request, "weather.html", context={"seven_days":will_weather, "weather":get_weather(city), "City":city})

def currency(request): return render(request, "currency.html", {"currencies":currencies})