
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    path('crea_tablero/', views.crea_tablero, name='crea_tablero'),
]