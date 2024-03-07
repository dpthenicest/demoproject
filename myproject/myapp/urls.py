from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('date_joined/', views.display_date),
  path('menu/', views.menu)
]