from django.contrib import admin
from django.urls import path
from hiveFeed.views import index, Feed, post_create_view, detail_post_View
from .views import UserRegisterView


urlpatterns = [
    path ('register/', UserRegisterView.as_view(), name = 'register'),

]
