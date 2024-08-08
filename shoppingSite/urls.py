

from shoppingSite import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mainPage/',views.mainPage, name='mainPage'),
    path('contact_us/',views.contactUs, name='contact_us'),
    path('about_us/',views.aboutUs, name='about_us'),
]