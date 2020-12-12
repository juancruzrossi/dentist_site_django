from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('administracion_ceo/', admin.site.urls),
    path('', include('website.urls')),
    path('', include('blog.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = 'website.views.error_404'