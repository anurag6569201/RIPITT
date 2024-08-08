from django.shortcuts import render
from django.shortcuts import redirect

from core.models import *
from django.shortcuts import get_object_or_404

def index(request):
    return redirect("core:home")

def home(request):
    testimonial=TestimonialModels.objects.all()
    service=ServiceModels.objects.all()
    context={
        'services':service,
        'testimonial':testimonial,
    }
    return render(request,"calling/pages.html",context)

def services(request,id):
    briefmodel = get_object_or_404(BreifServiceModels, pk=id)
    context={
        'briefmodel':briefmodel
    }
    return render(request,"calling/services.html",context)

def about(request):
    context={

    }
    return render(request,"calling/about.html",context)

def team(request):
    mentors=mentorsModels.objects.all()
    context={
       'mentors':mentors,
    }
    return render(request,"calling/team.html",context)

def event(request):
    return render(request,"calling/event.html")


def apply(request):
    return render(request,"calling/apply.html")


def construction(request):
    return render(request,"calling/construction.html")