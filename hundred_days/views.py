from django.shortcuts import render, redirect
import os
from .models import HProject
# Create your views here.
def hundred_days_home(request, page_number):
    hprojects = HProject.objects.order_by('-date')

    results_start_range = ((int(page_number) * 7) - 7)
    results_end_range = (int(page_number) * 7)

    hprojects_quantity = len(hprojects.all())
    correct_result_set = hprojects.all()[results_start_range:results_end_range]


    current_page = int(page_number)
    next_page = current_page
    next_next_page  =current_page
    previous_page = current_page
    last_page = hprojects_quantity//7
    if hprojects_quantity % 7 !=0:
        last_page+=1

    print(last_page, 'is the last_page')
    # check edge  cases  case 1: we we have less than three pages to display
    if last_page == 1:
         pass
    elif last_page ==  2 and current_page!=last_page:
         next_page= current_page  +  1
         last_page  =  next_page
    elif last_page == 3 and current_page!=last_page:
         next_page = current_page  +  1
         next_next_page  =  next_page + 1
         last_page = next_next_page
    else:
        if current_page!=last_page:
            next_page = current_page  +  1
            next_next_page = next_page + 1

    if current_page >1:
         previous_page = current_page - 1
         print(previous_page, 'is the previous_page')


    if previous_page ==1:#covers pages 1, 2, edge cases
        if last_page<3:
            return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':correct_result_set, 'hundred_days_page': 'hundred_days_page',  'current_page':current_page, 'page2':next_page,  'previous_page':previous_page, 'last_page': last_page})
        elif current_page == last_page:
            return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':correct_result_set, 'hundred_days_page': 'hundred_days_page',  'current_page':current_page, 'last_page':last_page, 'previous_page':previous_page})

        else:
            return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':correct_result_set, 'hundred_days_page': 'hundred_days_page',  'current_page':current_page, 'page2':next_page, 'page3':next_next_page, 'last_page':last_page, 'previous_page':previous_page})
    elif previous_page == 2:#covers third page edge case
        if last_page == 3:
            return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':correct_result_set, 'hundred_days_page': 'hundred_days_page', 'current_page':current_page,  'previous_page':previous_page, 'last_page':last_page})

    else:
        return render(request, os.path.join('hundred_days', 'hundred_days_home.html'), {'hprojects':correct_result_set, 'hundred_days_page': 'hundred_days_page', 'current_page':current_page, 'page2':next_page, 'page3':next_next_page, 'last_page':last_page, 'previous_page':previous_page})




def hundred_days_display_results(request, p_num, p_num_fix):
    return redirect('hundred_days_home', page_number = p_num_fix)
