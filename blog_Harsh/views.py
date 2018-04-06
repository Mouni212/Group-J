from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django import forms
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email =  userObj['email']
            password =  userObj['password']
            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                User.objects.create_user(username, email, password)
                user = authenticate(username = username, password = password)
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'blog/register.html', {'form' : form})



def post_list(request):
    return render(request, 'blog/post_list.html', {})


def product(request):
    return render(request, 'blog/product.html', {})


def career(request):
    return render(request, 'blog/career.html', {})



def contactus(request):
    return render(request, 'blog/contactus.html', {})


def edu(request):
    return render(request, 'blog/edu.html', {})

def aboutus(request):
    return render(request, 'blog/aboutus.html', {})


def news(request):
    return render(request, 'blog/news.html', {})

def distributor(request):
    return render(request, 'blog/distributor.html', {})    

def business(request):
    return render(request, 'blog/business.html', {}) 

def investor(request):
    return render(request, 'blog/investor.html', {}) 


def newsroom(request):
    return render(request, 'blog/newsroom.html', {})     


