from django.contrib import admin
from django.urls import path
from HelloApp import views
urlpatterns = [
    path('home/',views.home,name="Home"),
    path('blog/',views.blog,name="Blog"),
    path('contact/',views.contact,name="Contact"),
]
