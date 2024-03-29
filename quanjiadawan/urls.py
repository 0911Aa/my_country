"""quanjiadawan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,re_path
from company import views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('imgs/',views.img),
    path("get_img/",views.get_img),
    path('header/',views.header),
    path('test/',views.test),
    re_path(r'^video-(?P<classification_id>(\d+))-(?P<level_id>(\d+))-(?P<status>(\d+)).html$', views.video),
    url(r'^vedio2-(?P<direction_id>(\d+))-(?P<classification_id>(\d+))-(?P<level_id>(\d+)).html$', views.video2)
    ]
