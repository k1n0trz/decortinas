# Generated by Django 4.1.5 on 2023-05-05 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0010_pagina_product_galleryc_alter_product_galleryb_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="productogtitle",
            field=models.CharField(
                max_length=200, verbose_name="Metatítulo OG del Producto"
            ),
        ),
    ]
