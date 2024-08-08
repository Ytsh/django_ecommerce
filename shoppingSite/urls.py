

from shoppingSite import views
from django.urls import path


urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('mainPage/',views.mainPage, name='mainPage')
]