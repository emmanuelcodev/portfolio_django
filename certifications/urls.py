from django.urls import path
from . import views
import os

urlpatterns = [
    path('', views.certifications_homepage, name = "certifications_homepage"),
]
