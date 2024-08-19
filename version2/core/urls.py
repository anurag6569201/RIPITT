from django.urls import path
from core import views

app_name="core"

urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home,name="home"),
    path('services/<int:id>/', views.services, name="services"),
    path('about/',views.about,name="about"),
    path('team/',views.team,name="team"),
    path('event/',views.event,name="event"),
    path('apply/',views.apply,name="apply"),

    # demo pages
    path('construction/',views.construction,name="construction"),

    # chatbot
    path('send-message/', views.send_message, name='send_message'),
]