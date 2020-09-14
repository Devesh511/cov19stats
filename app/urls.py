from django.conf.urls import url
from django.urls import path, re_path
from app import views

urlpatterns = [
#   url(r'^$', views.profile, name='profile'),
    url(r'^notification$',views.notification, name='notification'),
    
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^hospital/$', views.hospital, name='hospital'),
    url(r'^hospital/details/$', views.details, name='details'),
   # url(r'^admin/', views.admin, name='admin'),
    url(r'^deaths/', views.deaths, name='deaths'),
      url(r'^$', views.home, name='home'),
]