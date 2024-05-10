from django.contrib import admin

from core.models import ServiceModels,QuoteModels,AboutCards,BreifServiceModels,WorkModels,TestimonialModels,ContactModels

admin.site.register(ServiceModels)
admin.site.register(BreifServiceModels)
admin.site.register(AboutCards)
admin.site.register(QuoteModels)
admin.site.register(WorkModels)
admin.site.register(TestimonialModels)
admin.site.register(ContactModels)