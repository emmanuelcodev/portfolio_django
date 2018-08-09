from django.shortcuts import render
import os
from .models import Certificate

#To Do
# Need to load images based on sets of 8 etc.... or else it will get infinitiely large
# put at bottom a  horizontal list of numbers 1,2,3... last  like on Amazon certifications_homepage
# when calling it from the homepage  always do{{ url 'name_of_url' 1}}  the one representing the 1st set 8 certificates
#once i have more ill put up more numbers


# Create your views here.
def certifications_homepage(request):
    certificates = Certificate.objects
    print(type(certificates.all))
    generator_list = generator_helper(certificates.all(),2)
    return render(request, os.path.join('certifications', 'certifications.html'), {'certificates_generator':generator_list, 'certificates_page':'certificates_page'})

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
