from . import views
from django.urls import path

urlpatterns = [
path('', views.details,name='details'),
path('details.html', views.details,name='details'),
    path('careerareas.html', views.careerareas,name='careerareas'),
path('About.html', views.About,name='About'),
path('jobs.html', views.jobs,name='jobs'),
path('<int:job_id>/', views.apply, name='apply'),
path('Apply.html', views.view,name='view'),
path('Application.html', views.apply,name='application'),
]