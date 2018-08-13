from django.urls import path
from . import views



urlpatterns = [
    path('', views.biography_home, name = 'biography_home'),
]
