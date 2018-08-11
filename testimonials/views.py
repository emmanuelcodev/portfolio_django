from django.shortcuts import render
import os
from .models import Testimonial
# Create your views here.


def testimonials_home(request):
    testimonies =  Testimonial.objects
    return render(request,os.path.join('testimonials', 'testimonials_home.html'),{ 'testimonials_page': 'testimonials_page', 'testimonies': testimonies})
