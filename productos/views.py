from django.shortcuts import render
from .models import Asesor, Product, Pagina, Comment, Video
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView
# from django.views.generic.base import RedirectView

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

class ProductDetailView(DetailView):
    model = Product
    template_name = 'producto-detalle.html'
    context_object_name = 'producto'

    def get_object(self):
        return Product.objects.get(producturl=self.kwargs['producturl'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.object.productogtitle
        context['keywords'] = self.object.productkeywords
        context['mdescription'] = self.object.productmetadesc
        context['ogurl'] = self.object.productogurl
        context['ogimg'] = self.object.productogimg
        context['ogtitle'] = self.object.productogtitle
        context['ogurlimg'] = self.object.productogurlsec
        context['ogdesc'] = self.object.productogdesc
        return context

def servicios(request):
    pagina_servicios = get_object_or_404(Pagina, pagename='Servicios')
    comments = Comment.objects.all()
    pageslogan = pagina_servicios.pageslogan
    pagetitle = pagina_servicios.pagetitle
    pagename = pagina_servicios.pagename
    pagebanner = pagina_servicios.pagebanner
    pagebannermov = pagina_servicios.pagebannermov
    pagemetatitle = pagina_servicios.pagemetatitle
    pageogtitle = pagina_servicios.pageogtitle
    pageogdesc = pagina_servicios.pageogdesc
    pagekeywords = pagina_servicios.pagekeywords
    pagemetadesc = pagina_servicios.pagemetadesc
    pageogurl = pagina_servicios.pageogurl
    pageogimg = pagina_servicios.pageogimg
    pageogurlsec = pagina_servicios.pageogurlsec
    return render(request, 'servicios.html', {
        'pagina': pagina_servicios,
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
        'pageslogan': pageslogan,
        'comments': comments,
        })

def pauta(request):
    pagina_pauta = get_object_or_404(Pagina, pagename='Pauta')
    comments = Comment.objects.all()
    pageslogan = pagina_pauta.pageslogan
    pagetitle = pagina_pauta.pagetitle
    pagename = pagina_pauta.pagename
    pagebanner = pagina_pauta.pagebanner
    pagebannermov = pagina_pauta.pagebannermov
    pagemetatitle = pagina_pauta.pagemetatitle
    pageogtitle = pagina_pauta.pageogtitle
    pageogdesc = pagina_pauta.pageogdesc
    pagekeywords = pagina_pauta.pagekeywords
    pagemetadesc = pagina_pauta.pagemetadesc
    pageogurl = pagina_pauta.pageogurl
    pageogimg = pagina_pauta.pageogimg
    pageogurlsec = pagina_pauta.pageogurlsec
    return render(request, 'pauta.html', {
        'pagina': pagina_pauta,
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
        'pageslogan': pageslogan,
        'comments': comments,
        })

def cookies(request):
    return render(request, 'cookies.html')

def privacy(request):
    return render(request, 'privacy.html')

def index(request):
    video =get_object_or_404(Video, videoname='Sheer Elegance')
    videourl = video.videourl
    pagina_home = get_object_or_404(Pagina, pagename='Home')
    pageslogan = pagina_home.pageslogan
    pagetitle = pagina_home.pagetitle
    pagename = pagina_home.pagename
    pagebanner = pagina_home.pagebanner
    pagebannermov = pagina_home.pagebannermov
    pagemetatitle = pagina_home.pagemetatitle
    pageogtitle = pagina_home.pageogtitle
    pageogdesc = pagina_home.pageogdesc
    pagekeywords = pagina_home.pagekeywords
    pagemetadesc = pagina_home.pagemetadesc
    pageogurl = pagina_home.pageogurl
    pageogimg = pagina_home.pageogimg
    pageogurlsec = pagina_home.pageogurlsec
    comments = Comment.objects.all()
    context= {
        'comments':comments,
        'pageogtitle': pageogtitle,
        'pageslogan': pageslogan,
        'pagetitle': pagetitle,
        'pagename': pagename,
        'pagebanner': pagebanner,
        'pagebannermov': pagebannermov,
        'pagemetatitle': pagemetatitle,
        'pageogdesc': pageogdesc,
        'pagekeywords': pagekeywords,
        'pagemetadesc': pagemetadesc,
        'pageogurl': pageogurl,
        'pageogimg': pageogimg,
        'pageogurlsec': pageogurlsec,
        'videourl':videourl,
    }
    return render(request, 'home.html', context)

def contacto(request):
    pagina_contacto = get_object_or_404(Pagina, pagename='Contacto')
    comments = Comment.objects.all()
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
        'pageslogan': pageslogan,
        'comments': comments,
        })

def nosotros(request):
    pagina_nosotros = get_object_or_404(Pagina, pagename='Nosotros')
    comments = Comment.objects.all()
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
        'pageslogan': pageslogan,
        'comments': comments,
        })

def comments(request):
    comments = Comment.objects.all()
    context = {
        'comments': comments,
    }
    return render(request, 'partials/comments.html', context)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

def robots(request):
    return render(request, 'robots.txt')