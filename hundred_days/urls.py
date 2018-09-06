from django.urls import path, include
from . import views


urlpatterns = [
    path('<int:page_number>/', views.hundred_days_home,name = 'hundred_days_home'),
    path('<int:p_num>/<int:p_num_fix>',views.hundred_days_display_results, name = 'hundred_days_page_fix'),

]
