from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('administracion_ceo/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('blog.urls')),
]


handler404 = 'website.views.error_404'