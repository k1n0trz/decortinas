from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto/', views.contacto, name="contacto"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('tienda/', views.tienda, name="tienda"),
    path('tienda/<str:producturl>/', views.producto, name="producto"),
    path('servicios/', views.servicios, name="servicios"),
    path('pauta/', views.pauta, name="pauta"),
    path('cookies/', views.cookies, name="cookies"),
    path('privacy/', views.privacy, name="privacy"),
]