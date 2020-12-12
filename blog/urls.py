from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.posts, name="blog"),
    path('blog/<slug:slug>', views.detallepost, name='detallepost'),
]