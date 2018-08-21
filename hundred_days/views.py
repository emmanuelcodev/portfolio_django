from django.shortcuts import render
import os
from .models import HProject
# Create your views here.
def hundred_days_home(request):
    hprojects = HProject.objects.order_by('-date')
    return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':hprojects, 'hundred_days_page': 'hundred_days_page' })
