from django.shortcuts import render
import os
from .models import Job

# Create your views here.

def home(request):
    jobs = Job.objects
    return render(request, os.path.join('jobs', 'home.html'), {'jobs':jobs})
