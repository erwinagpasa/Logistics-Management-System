from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

# from django.contrib.auth import views as auth_views

urlpatterns = [
  path('', include('core.urls')),
  path('', TemplateView.as_view(template_name="dashboard/index.html")),
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),  
]
