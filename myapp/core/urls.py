from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns = [
    path('', views.index, name='index'),
    path('venus/', views.venus, name='venus'),
]
