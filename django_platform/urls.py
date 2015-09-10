"""django_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url, patterns
from django.contrib import admin, auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from app.views import OrderListJson

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

]

urlpatterns += patterns('app.views',
                        url(r'^$', 'index', name='index'),
                        url(r'^login/$', 'loginApp', name='login'),
                        url(r'^logout/$', 'logoutApp', name='logout'),

                        url(r'^ajax_dict/', csrf_exempt(OrderListJson.as_view()), name='ajax-dict'),
                        url(r'^ajax_tem/', 'ajax_tem', name='ajax_tem'),
                        )