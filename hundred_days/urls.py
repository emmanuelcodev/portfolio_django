from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.hundred_days_home,name = 'hundred_days_home'),
]
