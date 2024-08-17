from asyncio.log import logger
from django.http import JsonResponse
from django.shortcuts import render
from django.shortcuts import redirect

from core.models import *
from django.shortcuts import get_object_or_404

import json
from django.views.decorators.csrf import csrf_exempt
from .chatbot import get_response


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


@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_message = data.get('message', '')
            if user_message:
                response_message = get_response(user_message)
                return JsonResponse({"reply": response_message})
            return JsonResponse({"reply": "I didn't understand that. Could you please rephrase?"})
        except json.JSONDecodeError as e:
            logger.error(f"JSON decode error: {e}")
            return JsonResponse({"error": "Invalid JSON format."}, status=400)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return JsonResponse({"error": "An unexpected error occurred."}, status=500)
    return JsonResponse({"error": "Invalid request method."}, status=405)