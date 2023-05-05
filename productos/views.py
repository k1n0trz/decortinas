from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Asesor, Product, Pagina
from django.shortcuts import get_object_or_404, render

# with open('productos/static/json/instant-jetty-384913-83fd70907d3d.json') as f:
#     data = json.load(f)

def tienda(request):
    # Resto del código para la función de vista
    productos = Product.objects.all()
    pagina_tienda = get_object_or_404(Pagina, pagename='Tienda')
    pageslogan = pagina_tienda.pageslogan
    pagetitle = pagina_tienda.pagetitle
    pagename = pagina_tienda.pagename
    pagebanner = pagina_tienda.pagebanner
    pagebannermov = pagina_tienda.pagebannermov
    pagemetatitle = pagina_tienda.pagemetatitle
    pageogtitle = pagina_tienda.pageogtitle
    pageogdesc = pagina_tienda.pageogdesc
    pagekeywords = pagina_tienda.pagekeywords
    pagemetadesc = pagina_tienda.pagemetadesc
    pageogurl = pagina_tienda.pageogurl
    pageogimg = pagina_tienda.pageogimg
    pageogurlsec = pagina_tienda.pageogurlsec
    return render(request, 'tienda.html', {
        'productos': productos,
        'pagemetatitle': pagemetatitle,
        'pageogtitle': pageogtitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl, 'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan
    })

# def producto(request, producturl):
#     product = get_object_or_404(Product, producturl=producturl)
#     return HttpResponse('product: %s' % product.producturl)

def producto(request, producturl):
    # Buscar el objeto Producto correspondiente al producturl
    producto = get_object_or_404(Product, producturl=producturl)
    titulo = producto.productogtitle
    ogtitle = producto.productogtitle
    ogdesc = producto.productogdesc
    keywords = producto.productkeywords
    mdescription = producto.productmetadesc
    ogurl = producto.productogurl
    ogimg = producto.productogimg
    ogurlimg = producto.productogurlsec
    # Renderizar la plantilla de detalle del producto y pasar el objeto producto como contexto
    return render(request, 'producto-detalle.html',{
        'producto': producto,
        'titulo': titulo,
        'keywords':keywords,
        'mdescription':mdescription,
        'ogurl':ogurl, 'ogimg':ogimg,
        'ogtitle':ogtitle,
        'ogurlimg':ogurlimg,
        'ogdesc':ogdesc})

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
    pagina_contacto = get_object_or_404(Pagina, pagename='Contacto')
    pageslogan = pagina_contacto.pageslogan
    pagetitle = pagina_contacto.pagetitle
    pagename = pagina_contacto.pagename
    pagebanner = pagina_contacto.pagebanner
    pagebannermov = pagina_contacto.pagebannermov
    pagemetatitle = pagina_contacto.pagemetatitle
    pageogtitle = pagina_contacto.pageogtitle
    pageogdesc = pagina_contacto.pageogdesc
    pagekeywords = pagina_contacto.pagekeywords
    pagemetadesc = pagina_contacto.pagemetadesc
    pageogurl = pagina_contacto.pageogurl
    pageogimg = pagina_contacto.pageogimg
    pageogurlsec = pagina_contacto.pageogurlsec
    return render(request, 'contacto.html', {
        'pagina': pagina_contacto,
        'pagemetatitle': pagemetatitle,
        'pageogtitle': pageogtitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan})

def nosotros(request):
    pagina_nosotros = get_object_or_404(Pagina, pagename='Nosotros')
    pageslogan = pagina_nosotros.pageslogan
    pagetitle = pagina_nosotros.pagetitle
    pagename = pagina_nosotros.pagename
    pagebanner = pagina_nosotros.pagebanner
    pagebannermov = pagina_nosotros.pagebannermov
    pagemetatitle = pagina_nosotros.pagemetatitle
    pageogtitle = pagina_nosotros.pageogtitle
    pageogdesc = pagina_nosotros.pageogdesc
    pagekeywords = pagina_nosotros.pagekeywords
    pagemetadesc = pagina_nosotros.pagemetadesc
    pageogurl = pagina_nosotros.pageogurl
    pageogimg = pagina_nosotros.pageogimg
    pageogurlsec = pagina_nosotros.pageogurlsec
    return render(request, 'nosotros.html', {
        'pagina': pagina_nosotros,
        'pagemetatitle': pagemetatitle,
        'pageogtitle': pageogtitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'pagebanner': pagebanner,
        'pagename': pagename,
        'pagebannermov': pagebannermov,
        'pagetitle': pagetitle,
        'pageslogan': pageslogan})