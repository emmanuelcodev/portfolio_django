from django.shortcuts import render
import os
# Create your views here.


def biography_home(request):
    return render(request, os.path.join('biography', 'biography_home.html'), {'biography_page': 'biography_page'})
