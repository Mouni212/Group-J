from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
    #url(r'^admin/', admin.site.urls),
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
