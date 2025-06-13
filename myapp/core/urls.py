from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('venus/', views.venus, name='venus'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('planet/<str:name>/', views.planet_detail, name='planet_detail'),
]
