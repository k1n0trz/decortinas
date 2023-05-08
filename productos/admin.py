from django.contrib import admin
from .models import Asesor, Product, Pagina, Comment

# Register your models here.
admin.site.register(Asesor)
admin.site.register(Product)
admin.site.register(Pagina)
admin.site.register(Comment)