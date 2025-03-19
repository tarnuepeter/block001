from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('read-detail/<str:slug>/', views.read_detail, name='read-detail'),
]