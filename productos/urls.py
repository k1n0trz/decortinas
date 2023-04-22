from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('nosotros/', views.nosotros),
    path('tienda/', views.tienda),
    path('tienda/<str:producturl>', views.producto),
    path('contacto/', views.contacto),
]