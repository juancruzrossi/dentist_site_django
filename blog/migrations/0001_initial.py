# Generated by Django 3.1.4 on 2020-12-12 03:54

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60, verbose_name='Título del post')),
                ('slug', models.CharField(max_length=25, verbose_name='Slug')),
                ('descripcion', models.CharField(max_length=60, verbose_name='Breve descripción del post')),
                ('imagen', models.URLField(max_length=255)),
                ('contenido', ckeditor.fields.RichTextField()),
                ('publicado', models.BooleanField(default=True, verbose_name='Publicar')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='Fecha De Creación')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['id'],
            },
        ),
    ]
