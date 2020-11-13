from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls), #main path called the URL
    url('', include('ticketing_api.urls')),
    
]
