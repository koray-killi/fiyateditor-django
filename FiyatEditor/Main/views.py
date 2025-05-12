# Imports necessary models and ImageCreation class from 'utils.py'
from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from Main.models import Sebze, PriceList
from Main.utils import ImageCreation

# Create your views here.


## This form is a main form of the application.
## It basically handle the POST requests which is identified by Sebze.name.
## After identifying, it converts the 'Sebze' type object to 'PriceList' type object, which is suitable for using utils.py's methods.
## Lastly it seperates the new objects into their types and collects the output in the dictionary which nested by lists.
## While handling the dictionary, it changes and save the status of price in DB.

def index_form(request):
    formatted_dict = {}
    baslik = str()
    for SebzeObject in Sebze.objects.all():
        formatted_dict[SebzeObject.type] = []
    if request.method == "POST":
        baslik = request.POST.get('date')
        for SebzeObject in Sebze.objects.all():
            object = PriceList(SebzeObject.name,SebzeObject.type,float(request.POST.get(f'{SebzeObject.name}-once')),float(request.POST.get(f'{SebzeObject.name}-bugun')))
            formatted_dict[SebzeObject.type].append(object)
            SebzeObject.price = object.today_price
            SebzeObject.save()
    ImageCreation.CreateImage(baslik,formatted_dict)
    return redirect('success/')


# To get specific-type objects in single-list, we use filter method.
def index(response):
    return render(response,'index.html',{
        "biberler": Sebze.objects.filter(type="biber"),
        "domatesler": Sebze.objects.filter(type="domates"),
        "salataliklar": Sebze.objects.filter(type="salatalik"),
        "patlicanlar": Sebze.objects.filter(type="patlican"),
        "kabaklar": Sebze.objects.filter(type="kabak"),
        
    })

def success(response):
    return render(response, 'success.html')