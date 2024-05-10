from django.contrib import admin

from core.models import ServiceModels,QuoteModels,AboutCards,BreifServiceModels

admin.site.register(ServiceModels)
admin.site.register(BreifServiceModels)
admin.site.register(AboutCards)
admin.site.register(QuoteModels)