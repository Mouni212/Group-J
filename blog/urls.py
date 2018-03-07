from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
     url(r'^product$', views.product, name='product'),
      url(r'^career$', views.career, name='career'),
       url(r'^contactus$', views.contactus, name='contactus'),
        url(r'^aboutus$', views.aboutus, name='aboutus'),
         url(r'^news$', views.news, name='news'),
         url(r'^edu$', views.edu, name='edu'),
         url(r'^distributor$', views.distributor, name='distributor'),
         url(r'^business$', views.business, name='business'),
         url(r'^investor$', views.investor, name='investor'),
         url(r'^newsroom$', views.newsroom, name='newsroom'),
]
