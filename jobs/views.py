from django.shortcuts import render
import os
from .models import Job

# Create your views here.

def home(request):
    jobs = Job.objects
    #for x,y in request.META.items():
        #print(x, ' : ', y)
    return render(request, os.path.join('jobs', 'home.html'), {'jobs':jobs})
