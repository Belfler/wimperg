from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wimperg.urls', namespace='wimperg')),
    path('', include('django.contrib.auth.urls')),
    path('social-auth/', include('social_django.urls', namespace='social'))
]
