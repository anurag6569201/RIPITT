from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return redirect("core:home")

def home(request):
    context={
        
    }
    return render(request,"calling/pages.html",context)

def services(request):
    return render(request,"calling/services.html")