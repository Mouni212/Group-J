from django.shortcuts import render

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