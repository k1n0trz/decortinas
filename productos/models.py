from django.db import models
from ckeditor.fields import RichTextField
from storages.backends.gcloud import GoogleCloudStorage

# Create your models here.
class Asesor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model): # Crea la tabla product en db
    # Elementos del header del producto
    productmetadesc = models.CharField(max_length=200, verbose_name="Meta descripción del Producto")
    productkeywords = models.CharField(max_length=200, verbose_name="Palabras clave del Producto")
    # Elementos OG del producto
    productogdesc = models.CharField(max_length=200, verbose_name="Descripción OG del Producto")
    productogtitle = models.CharField(max_length=200, verbose_name="Titulo OG del Producto")
    productogurl = models.CharField(max_length=200, verbose_name="Url OG del Producto")
    productogimg = models.CharField(max_length=200, verbose_name="Url OG Microformato del Producto")
    productogurlsec = models.CharField(max_length=200, verbose_name="Url OG Segura del Producto")
    # Elementos Visuales del producto
    productname = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    productslogan = models.CharField(max_length=200, verbose_name="Slogan del Producto")
    productoldprice = models.IntegerField(verbose_name="Precio normal")
    productdiscount = models.IntegerField(verbose_name="Valor de descuento")
    producturl = models.CharField(max_length=200, verbose_name="Url producto detalle")
    productdescription = RichTextField()
    productimg = models.ImageField(
        upload_to='uploads/',
        storage=GoogleCloudStorage(),
        verbose_name='Imagen principal del Producto'
    )
    # productimg = models.ImageField(upload_to='static/img/uploads/', verbose_name="Imagen principal del Producto")
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)
    productprice = models.IntegerField(verbose_name="Precio de venta", blank=True, null=True, editable=False)

    def __str__(self):
        return self.productname + ' - creado por - ' + self.asesor.name

    def save(self, *args, **kwargs):
        if self.productoldprice and self.productdiscount:
            self.productprice = self.productoldprice - (self.productoldprice * self.productdiscount / 100)
        super().save(*args, **kwargs)

# class Product(models.Model):
#     productname = models.CharField(max_length=200, verbose_name="Nombre del Producto")
#     productoldprice = models.IntegerField(verbose_name="Precio normal")
#     productprice = models.IntegerField(verbose_name="Precio de venta")
#     productdiscount = models.IntegerField(verbose_name="Precio de venta")
#     producturl = models.CharField(max_length=200, verbose_name="Url producto detalle")
#     productdescription = RichTextField()
#     productimg = models.ImageField(upload_to='static/img/uploads/', verbose_name="Imagen principal del producto")
#     asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)

#     def __str__(self):
#         return self.productname + ' - creado por - ' + self.asesor.name
