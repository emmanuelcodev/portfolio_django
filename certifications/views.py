from django.shortcuts import render, redirect
import os
from .models import Certificate

#To Do
# Need to load images based on sets of 8 etc.... or else it will get infinitiely large
# put at bottom a  horizontal list of numbers 1,2,3... last  like on Amazon certifications_homepage
# when calling it from the homepage  always do{{ url 'name_of_url' 1}}  the one representing the 1st set 8 certificates
#once i have more ill put up more numbers



# Create your views here.
def certifications_homepage(request, page_number):
    # figure out exactly which set of certificates to display pending on the page number the user request, 7 results for each page
    results_start_range = ((int(page_number) * 7) - 7)
    results_end_range = (int(page_number) * 7)
    print('s ', results_start_range)
    print('e ', results_end_range)

    # grab certificates from database
    certificates = Certificate.objects #  get object manager
    certificate_quantity = len(certificates.all()) #get number of certificates in our db
    correct_result_set = certificates.all()[results_start_range:results_end_range]# get certificate only  in our results range as requested by the user


    #Find correct page numbers for the bottom  page navigation links
    current_page = int(page_number)
    next_page = current_page
    next_next_page  =current_page
    previous_page = current_page
    last_page = certificate_quantity//7
    if certificate_quantity % 7 !=0:
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
    #else do nothing because we only have one page




    #  pass results
    generator_list = generator_helper(correct_result_set, 2)

    # pass dictionary holding page numbers to  display, assumes you have atleast one object
    page_numbers_dic ={}
    page_numbers_dic['page1']=current_page
    if next_page >1:
        page_numbers_dic['page2']=next_page
    if next_next_page > 2:
        page_numbers_dic['page3']=next_next_page
    page_numbers_dic['page4']=last_page



    '''
    print('\n\n\n Now showing stuff:\n', correct_result_set,'\n\n\n')
    print(certificates.all())
    print(certificate_quantity)
    pages = certificate_quantity/7 #how many sets of 7
    if certificate_quantity % 7 !=0:
        pages+=1

    print('pages', pages, ' quantity ', certificate_quantity)

    generator_list = generator_helper(certificates.all(),2)
    '''

    if previous_page ==1:#covers pages 1, 2, edge cases
        if last_page<3:
            return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page', 'current_page':current_page, 'page2':next_page,  'previous_page':previous_page, 'last_page': last_page})
        elif current_page == last_page:
            return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page', 'current_page':current_page, 'last_page':last_page, 'previous_page':previous_page})

        else:
            return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page', 'current_page':current_page, 'page2':next_page, 'page3':next_next_page, 'last_page':last_page, 'previous_page':previous_page})
    elif previous_page == 2:#covers third page edge case
        if last_page == 3:
            return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page', 'current_page':current_page,  'previous_page':previous_page, 'last_page':last_page})



    else:
        return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page', 'current_page':current_page, 'page2':next_page, 'page3':next_next_page, 'last_page':last_page, 'previous_page':previous_page})

def generator_helper(abritrary_object, n_chunk_size):
    '''  takes an interval object and returns a generator made up of n size list groups
    SO 1...100, N = 2 --> (1,2), (3,4),(5,6) etc.... (99,100)
    Yield successive n-sized chunks from l.
    '''
    """Yield successive n-sized chunks from l."""
    '''    x = 0
    for x in abritrary_object:
        print(x)
    '''
    length_object = len(abritrary_object)
    if n_chunk_size == 2:
        if length_object % 2: # if even sets continue as normal
            for i in range(0,length_object, n_chunk_size):
                yield  abritrary_object[i:i + n_chunk_size]
        else:#  nothing exists after last I object so need to return I nothing more
            for i in range(0,length_object, n_chunk_size):
                if i== length_object:
                    yield  [abritrary_object[i]]
                else:
                    yield abritrary_object[i:i + n_chunk_size]
    else:
        for i in range(0,length_object, n_chunk_size):
            yield  abritrary_object[i:i + n_chunk_size]



#fix to display pages , will just redirect to certifications_homepage
def certificate_display_results(request, p_num, p_num_fix):

    return redirect('certifications_homepage', page_number = p_num_fix)
