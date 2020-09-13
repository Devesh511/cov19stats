from django.conf.urls import url
from django.urls import path, re_path
from app import views

urlpatterns = [
   url(r'^$', app_views.profile, name='profile'),
    url(r'^notification$',app_views.notification, name='notification'),
    
    url(r'^contact/$', app_views.contact, name='contact'),
    url(r'^hospital/$', app_views.hospital, name='hospital'),
    url(r'^admin/', app_views.admin, name='admin'),
    url(r'^edit/', app_views.update_user, name='update_user'),
]