from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('read-detail', views.read_detail, name='read-detail'),
]