
from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [


    url(r'signup',signup_view),
    url(r'login',login_view),
    url(r'feed' , feed),
    url(r'post', post_view),
    url(r'like', like_view),
    url(r'comment', comment_view),
]
