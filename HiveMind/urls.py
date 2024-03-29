"""HiveMind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from hiveFeed.views import index, Feed, post_create_view, detail_post_View, Hidden


urlpatterns = [
    path ('', index, name='home'),
    path ('feed/', Feed.as_view(), name='feed'),
    path ('post/', post_create_view, name= 'create'),
    path('admin/', admin.site.urls),
    path ('post/<int:pk>', detail_post_View.as_view(), name= 'view'),
    path ('members/', include('django.contrib.auth.urls')),
    path ('member/', include('members.urls')),
    path ('VGhpc2lzaGlkZGVuYmlndGltZQ/', Hidden, name='hidden')
]
