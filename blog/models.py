from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    titulo = models.CharField('Título del post', max_length=60, blank=False, null=False)
    slug = models.CharField('Slug', max_length=25, blank=False, null=False)
    descripcion = models.CharField('Breve descripción del post', max_length=60, blank=False, null=False)
    imagen = models.URLField(max_length=255, blank=False, null=False)
    contenido = RichTextField()
    publicado = models.BooleanField('Publicar', default=True)
    fecha_creacion = models.DateField('Fecha De Creación', auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
        
    def __str__(self):
        return self.titulo