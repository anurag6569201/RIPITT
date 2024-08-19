from core.models import ContactModels

def contactview(request):
    contact=ContactModels.objects.first()
    context= {
        'contact':contact,
    }
    return context