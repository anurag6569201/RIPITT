from django.shortcuts import render
from django.shortcuts import redirect

from core.models import ServiceModels,QuoteModels

def index(request):
    return redirect("core:home")

def home(request):
    service=ServiceModels.objects.all()
    context={
        'services':service
    }
    return render(request,"calling/pages.html",context)

def services(request):
    return render(request,"calling/services.html")

def about(request):
    quotes=QuoteModels.objects.all()
    context={
        'quoters':quotes,
    }
    return render(request,"calling/about.html",context)