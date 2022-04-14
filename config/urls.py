from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', include('core.urls')), #Match everything in core app
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),  
]
