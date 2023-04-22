from django.db import models

# Create your models here.
class Asesor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model): # Crea la tabla product en db
    productname = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    productoldprice = models.CharField(max_length=200, verbose_name="Precio normal")
    productprice = models.CharField(max_length=200, verbose_name="Precio de venta")
    productdiscount = models.CharField(max_length=200, verbose_name="Valor de descuento")
    producturl = models.CharField(max_length=200, verbose_name="Url producto detalle")
    productdescription = models.TextField()
    productimg = models.ImageField(upload_to='img/', verbose_name="Imagen principal del producto")
    asesor = models.ForeignKey(Asesor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.productname + ' - creado por - ' + self.asesor.name
