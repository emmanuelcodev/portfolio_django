from django.urls import path
from . import views
import os

urlpatterns = [
    path('<int:page_number>/', views.certifications_homepage, name = "certifications_homepage"),
    path('<int:p_num>/<int:p_num_fix>',views.certificate_display_results, name = 'certificate_page_fix')
]
