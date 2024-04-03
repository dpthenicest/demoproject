from django.urls import path
from . import views

urlpatterns = [
  # path('', views.home, name='home'),
  path('date_joined/', views.display_date, name='date_joined'),
  path('menu/', views.menu, name='menu'),
  path('path/', views.path, name='path'),
  path('req_info/', views.request_info, name='request_info'),
  path('dishes/<str:dish>/', views.menuitems, name='dishes_dish'),
  path('shifts/', views.form_view),
  path('log/', views.log_view)
]