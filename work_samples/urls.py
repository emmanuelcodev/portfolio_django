from django.urls import path
from . import views
import os

urlpatterns = [
    path('<int:project_id>/', views.home_int, name='work_samples_int'),
]
