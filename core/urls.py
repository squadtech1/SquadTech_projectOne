from django.urls import path

from .views import index, login, cadastro


urlpatterns = [
    path('', index),
    path('login', login),
    path('cadastro', cadastro),
]
