from django.urls import path
from . import views

urlpatterns = [
    
    #creates a url for redirecting to the home of farmer education
    path('',views.BlogListView.as_view()),
    
    #creates a url for displaying individual blogs
    path('<int:pk>',views.BlogDetailView.as_view(),name='detail_post_view')
]