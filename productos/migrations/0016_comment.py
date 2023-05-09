# Generated by Django 4.1.5 on 2023-05-08 14:36

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("productos", "0015_alter_pagina_pageogtitle"),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "commentname",
                    models.CharField(max_length=200, verbose_name="Nombre del usuario"),
                ),
                (
                    "commentplace",
                    models.CharField(
                        blank=True, max_length=200, verbose_name="Orígen del usuario"
                    ),
                ),
                (
                    "commentimg",
                    models.ImageField(
                        default="/productos/static/img/no-comment.png",
                        upload_to="imagenes-decortinas/",
                        verbose_name="Imagen Banner del usuario",
                    ),
                ),
                (
                    "commentdescription",
                    ckeditor.fields.RichTextField(
                        verbose_name="Comentario del usuario"
                    ),
                ),
                (
                    "commentqualify",
                    models.IntegerField(
                        choices=[
                            (1, "1 estrella"),
                            (2, "2 estrellas"),
                            (3, "3 estrellas"),
                            (4, "4 estrellas"),
                            (5, "5 estrellas"),
                        ],
                        default=1,
                        verbose_name="Calificación del usuario",
                    ),
                ),
            ],
        ),
    ]