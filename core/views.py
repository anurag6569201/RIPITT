from django.shortcuts import render
from django.shortcuts import redirect

from core.models import ServiceModels,QuoteModels,AboutCards,BreifServiceModels
from django.shortcuts import get_object_or_404

def index(request):
    return redirect("core:home")

def home(request):
    cards=AboutCards.objects.all()
    service=ServiceModels.objects.all()
    context={
        'services':service,
        'aboutcards':cards
    }
    return render(request,"calling/pages.html",context)

def services(request,id):
    briefmodel = get_object_or_404(BreifServiceModels, pk=id)
    context={
        'briefmodel':briefmodel
    }
    return render(request,"calling/services.html",context)

def about(request):
    quotes=QuoteModels.objects.all()
    context={
        'quoters':quotes,
    }
    return render(request,"calling/about.html",context)