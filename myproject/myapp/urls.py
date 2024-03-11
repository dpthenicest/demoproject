from django.urls import path
from . import views

urlpatterns = [
  path('', views.home),
  path('date_joined/', views.display_date),
  path('menu/', views.menu),
  path('path/', views.path),
  path('req_info', views.request_info),
  path('dishes/<str:dish>', views.menuitems)
]