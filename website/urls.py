from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register_item', views.register_item,name='register_item')
]