from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venus/', views.venus, name='venus'),
]
