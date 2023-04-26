from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Asesor, Product
from django.shortcuts import get_object_or_404, render
import json
# import json

# with open('productos/static/json/instant-jetty-384913-83fd70907d3d.json') as f:
#     data = json.load(f)

def tienda(request):
    # Lee el contenido del archivo JSON
    with open('productos/static/json/instant-jetty-384913-83fd70907d3d.json', 'r') as f:
        data = json.load(f)
    # Resto del código para la función de vista
    productos = Product.objects.all()
    return render(request, 'tienda.html', {
        'productos': productos,
        'data': data,
    })

# def producto(request, producturl):
#     product = get_object_or_404(Product, producturl=producturl)
#     return HttpResponse('product: %s' % product.producturl)

def producto(request, producturl):
    # Buscar el objeto Producto correspondiente al producturl
    producto = get_object_or_404(Product, producturl=producturl)
    titulo = producto.productname
    ogtitle = producto.productogtitle
    ogdesc = producto.productogdesc
    keywords = producto.productkeywords
    mdescription = producto.productmetadesc
    ogurl = producto.productogurl
    ogimg = producto.productogimg
    ogurlimg = producto.productogurlsec
    # Renderizar la plantilla de detalle del producto y pasar el objeto producto como contexto
    return render(request, 'producto-detalle.html',{'producto': producto, 'titulo': titulo, 'keywords':keywords, 'mdescription':mdescription, 'ogurl':ogurl, 'ogimg':ogimg, 'ogtitle':ogtitle, 'ogurlimg':ogurlimg, 'ogdesc':ogdesc})

def servicios(request):
    return render(request, 'servicios.html')

def pauta(request):
    return render(request, 'pauta.html')

def cookies(request):
    return render(request, 'cookies.html')

def privacy(request):
    return render(request, 'privacy.html')

def index(request):
    return render(request, 'home.html')

def contacto(request):
    return render(request, 'contacto.html')

def nosotros(request):
    return render(request, 'nosotros.html')