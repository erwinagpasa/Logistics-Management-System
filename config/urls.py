from django.contrib import admin
from django.urls import include, path
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
  path('', include('core.urls')), #Match everything in core app
  path('admin/', admin.site.urls),
  path('accounts/', include('allauth.urls')),  
]
# Serving static files
# urlpatterns += staticfiles_urlpatterns()
