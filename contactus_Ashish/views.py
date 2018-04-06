from django.shortcuts import render
#from django.views.generic import TemplateView
# Create your views here.

def ContactPage(request):
    return render(request,'contactus/contactuspage.html')
