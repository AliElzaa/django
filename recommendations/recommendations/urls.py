"""recommendations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.conf.urls import url
from rewards import views


urlpatterns = [
    #path('admin/', admin.site.urls),
    url('getOrders/(?P<user_id>[0-9]*)', views.get_orders_view),
    url('users/', views.get_users_view),
    url("get_points/(?P<user_id>[0-9]*)", views.get_users_points_view),
    url("sp_user/(?P<user_id>[0-9]*)", views.get_specific_view),
    url("recommendations/(?P<user_id>[0-9]*)", views.recommendations_view )
]
