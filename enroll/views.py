from django.shortcuts import render
from .forms import StudentRegistration

# Create your views here.
def showformdata(request):
    # Runtime initialization
    form = StudentRegistration(initial={'name': 'Kazi Mushfiqur Rahman'}) 
    return render(request, 'enroll/userregistration.html',
                  {'form': form})
