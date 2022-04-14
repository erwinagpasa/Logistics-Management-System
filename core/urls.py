from django.urls import path, re_path
from . import views



urlpatterns = [
  path('accounts/profile/', views.profile, name="profile"),
]
