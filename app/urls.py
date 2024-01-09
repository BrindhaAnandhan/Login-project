#from django.contrib import admin
from django.urls import path
from app.views import *
app_name = "app"

urlpatterns = [
    path('',home, name="home"),
    path("signin/", signin, name = "signin"),
    path("signup/", signup, name = "signup"),
    path("signout/", signout, name = "signout"),
]