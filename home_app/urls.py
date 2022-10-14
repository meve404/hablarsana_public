from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_app, name='home-app'),
    path('professional-background/', views.profesional_bg, name='professional-background'),
    path('testimonies/', views.testimonies, name='testimonies'),
]
