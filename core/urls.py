from django.urls import path, re_path
from . import views



urlpatterns = [
  path('', views.home, name="home"),
  path('accounts/profile/', views.profile, name="profile"),
  path('dashboard/', views.dashboard, name='dashboard'),
]
