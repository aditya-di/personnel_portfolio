from django.shortcuts import render
from .models import Job

# Create your views here.
def user(request):
    jobs= Job.objects
    return render(request,'jobs/adityadi.html',{'jobs':jobs})
    


