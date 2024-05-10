from django.urls import path
from core import views

app_name="core"

urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home,name="home"),
    path('services/<int:id>', views.services, name="services"),
    path('about/',views.about,name="about"),
]