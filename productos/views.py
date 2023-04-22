from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Asesor, Product
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def contacto(request):
    return HttpResponse("Nosotros somos Decortinas")

def nosotros(request):
    return render(request, 'nosotros.html')

def tienda(request):
    #tienda = list(Asesor.objects.values())
    productos = Product.objects.all()
    return render(request, 'tienda.html', {
        'productos': productos
    })

def producto(request, producturl):
    product = get_object_or_404(Product, producturl=producturl)
    return HttpResponse('product: %s' % product.producturl)
