from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/candidato/', views.register_candidate, name='register_candidate'),
]