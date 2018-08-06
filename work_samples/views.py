from django.shortcuts import render, get_object_or_404, redirect
import os
from .models import WorkSamples
# Create your views here.

def home_int(request, project_id):
    project = get_object_or_404(WorkSamples, pk = project_id)
    return render(request, os.path.join('work_samples', 'work_samples.html'), {'work_samples_page':'work_samples_page', 'project':project})
