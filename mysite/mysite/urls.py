"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles
from django.conf.urls import url
from django.contrib import admin

from website.views.views import *

########################

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    #########################
    url(r'^hello/$', hello),
    url(r'^project/$', project),
    url(r'^search/$', search),
    url(r'^recommend/$', recommend),
    url(r'^find/$', find),
    url(r'^homepage/$', homepage),
    url(r'^restaurant/$',restaurant),
    url(r'^analysis/$',analysis),
    #########################
]
urlpatterns += staticfiles_urlpatterns()