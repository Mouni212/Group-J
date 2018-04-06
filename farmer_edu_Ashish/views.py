
from django.views.generic import ListView,DetailView
from . models import Post

# Create your views here.

#creates a view for viewing farmer education home page and list of blogs
class BlogListView(ListView):
    model = Post
    template_name='farmer_edu/farmer_edu_home.html'

#creates a view for viewing individual blogs
class BlogDetailView(DetailView):
    model=Post
    template_name='farmer_edu/post_detail.html'
