from django.http import HttpResponse
from django.shortcuts import render
from .models import Jobs

# Create your views here.
def details(request):
    return render(request,'.\careers\details.html')
def careerareas(request):
    return render(request,'.\careers\careerareas.html')
def About(request):
    return render(request,'.\careers\About.html')
def jobs(request):
    all_jobs=Jobs.objects.all()
    context={'all_jobs':all_jobs}
    return render(request,'.\careers\jobs.html',context)
def apply(request):

    return render(request, '.\careers\Application.html')
def view(request):
    return render(request,'.\careers\Apply.html')