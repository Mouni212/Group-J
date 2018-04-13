from django.shortcuts import render
from django.utils import timezone
from .models import Post
def faq(request):
    posts = Post.objects.all()
    return render(request, 'faq1/faq.html', {'posts': posts})
