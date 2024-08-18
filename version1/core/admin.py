from django.contrib import admin

from core.models import ServiceModels,BreifServiceModels,TestimonialModels,ContactModels,mentorsModels

admin.site.register(ServiceModels)
admin.site.register(BreifServiceModels)
admin.site.register(TestimonialModels)
admin.site.register(ContactModels)

class mentorServiceModels(admin.ModelAdmin):
    list_display = ('name', 'order')

admin.site.register(mentorsModels, mentorServiceModels)