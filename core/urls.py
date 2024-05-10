from django.urls import path
from core import views

app_name="core"

urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home,name="home"),
    path('services/<int:id>', views.services, name="services"),
    path('about/#slide02',views.about,name="about"),

    # demo pages
    path('construction/',views.construction,name="construction"),
]