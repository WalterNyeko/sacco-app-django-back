"""vastech_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from authentication.views import (change_passowrd, password_reset)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('', include('roles.urls')),
    url('api/', include('profiles.urls')),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url('api/', include('authentication.urls')),
    url(r'^api/set_password/complete/',
        change_passowrd, name='change_passowrd'
        ),
    url(r'^api/password_reset/', password_reset, name='password'),
]
