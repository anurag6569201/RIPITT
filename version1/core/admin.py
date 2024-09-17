from django.contrib import admin

from core.models import ServiceModels,BreifServiceModels,TestimonialModels,ContactModels,mentorsModels,ScrollContenModel

admin.site.register(ServiceModels)
admin.site.register(BreifServiceModels)
admin.site.register(TestimonialModels)
admin.site.register(ContactModels)
admin.site.register(ScrollContenModel)

admin.site.register(mentorsModels)