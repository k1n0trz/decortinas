from django.db import models
from ckeditor.fields import RichTextField
from storages.backends.s3boto3 import S3Boto3Storage
from django.urls import reverse
from django.utils import timezone

# Create your models here.
class Asesor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class S3ProductImage(S3Boto3Storage):
    location = 'imagenes-decortinas'
    file_overwrite = False

class Product(models.Model):
    # Elementos del header del producto
    productmetadesc = models.CharField(max_length=200, verbose_name="Meta descripción del Producto")
    productkeywords = RichTextField(verbose_name="Palabras clave del Producto")
    productbanner = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner del Producto", default='/productos/static/img/default.jpg')
    productbannermov = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner del Producto en Móvil", default='/productos/static/img/default-mov.jpg')
    # Elementos OG del producto
    productogdesc = models.CharField(max_length=200, verbose_name="Descripción OG del Producto")
    productogtitle =models.CharField(max_length=200, verbose_name="Metatítulo OG del Producto")
    productogurl = models.CharField(max_length=200, verbose_name="Url OG del Producto")
    productogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato del Producto")
    productogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura del Producto")
    # Elementos Visuales del producto
    productname = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    productslogan = models.CharField(max_length=200, verbose_name="Slogan del Producto")
    productoldprice = models.IntegerField(verbose_name="Precio normal", blank=True, default=0, null=True)
    productdiscount = models.IntegerField(verbose_name="Valor de descuento", blank=True, default=0, null=True)
    producturl = models.CharField(max_length=200, verbose_name="Url producto detalle")
    productdescription = RichTextField()
    productimg = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen principal del Producto")
    gallerya = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen secundaria del Producto", blank=True)
    galleryb = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen adicional del Producto", blank=True)
    galleryc = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen final del Producto", blank=True)
    # productimg = models.ImageField(upload_to='static/img/uploads/', verbose_name="Imagen principal del Producto")
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)
    productprice = models.IntegerField(verbose_name="Precio de venta", blank=True, null=True, editable=False)
    productupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.productname + ' - creado por - ' + self.asesor.name

    def save(self, *args, **kwargs):
        self.productupdated = timezone.now()
        if self.productoldprice is not None and self.productdiscount is not None:
            self.productprice = self.productoldprice - (self.productoldprice * self.productdiscount / 100)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

class Pagina(models.Model):
    pagename = models.CharField(max_length=200, verbose_name="Nombre de la página")
    pagemetatitle = models.CharField(max_length=200, verbose_name="Metatítulo(title) de la página")
    pagetitle = models.CharField(max_length=200, verbose_name="Título(h1) de la página")
    pageslogan = models.CharField(max_length=200, verbose_name="Slogan(h2) de la página")
    pagemetadesc = models.CharField(max_length=200, verbose_name="Meta descripción de la página")
    pagekeywords = RichTextField(verbose_name="Palabras clave de la página")
    pagebanner = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner de la página", default='/productos/static/img/default.jpg')
    pagebannermov = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner de la página en Móvil", default='/productos/static/img/default-mov.jpg')
    pageogdesc = models.CharField(max_length=200, verbose_name="Descripción OG de la página")
    pageogtitle = models.CharField(max_length=200, verbose_name="Título OG de la página")
    pageogurl = models.CharField(max_length=200, verbose_name="Url OG de la página")
    pageogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato de la página")
    pageogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura de la página")

    def __str__(self):
        return self.pagename
    
class Comment(models.Model):
    ONE_STAR = 1
    TWO_STARS = 2
    THREE_STARS = 3
    FOUR_STARS = 4
    FIVE_STARS = 5

    RATING_CHOICES = [
        (ONE_STAR, '1 estrella'),
        (TWO_STARS, '2 estrellas'),
        (THREE_STARS, '3 estrellas'),
        (FOUR_STARS, '4 estrellas'),
        (FIVE_STARS, '5 estrellas'),
    ]

    commentname = models.CharField(max_length=200, verbose_name="Nombre del usuario")
    commentplace = models.CharField(max_length=200, verbose_name="Orígen del usuario", blank=True)
    commentimg = models.ImageField(upload_to='imagenes-decortinas/', verbose_name="Imagen Banner del usuario", default='/productos/static/img/no-comment.png')
    commentdescription = RichTextField(verbose_name="Comentario del usuario")
    commentqualify = models.IntegerField(choices=RATING_CHOICES, default=ONE_STAR, verbose_name="Calificación del usuario")

    def __str__(self):
        return self.commentname
    
class Video(models.Model):
    videoname = models.CharField(max_length=200, verbose_name="Nombre del video")
    videourl = models.CharField(max_length=200, verbose_name="URL del video")

    def __str__(self):
        return self.videoname