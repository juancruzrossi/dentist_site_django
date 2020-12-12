from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Post

from django.db.models import Q
from django.core.paginator import Paginator

def posts(request):
    """ Queryset de la seccion del /blog """
    posts_blog = Post.objects.filter(publicado=True).order_by('-id')
    
    """ Queryset para buscar posts"""
    queryset = request.GET.get("buscar")
    
    if queryset:
        posts_blog = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset) | Q(contenido__icontains = queryset)).distinct()
    
    """ Queryset de la seccion de ultimos 3 posts que aparecen a la izquierda """
    posts = Post.objects.filter(publicado=True).order_by('?')[:4]
    
    """ Paginacion """
    paginator = Paginator(posts_blog, 5)
    page = request.GET.get('page')
    posts_blog = paginator.get_page(page)
    
    
    
    return render(request, 'blog.html', {'posts_blog':posts_blog, 'posts':posts})


def detallepost(request, slug):

    """ Queryset de cada post segun su slug """
    post = get_object_or_404(Post, slug=slug)

    """ Queryset de la seccion de ultimos 3 posts que aparecen a la izquierda """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:4]
    
    """ Queryset para buscar posts"""
    queryset = request.GET.get("buscar")
    
    if queryset:
        posts_blog = Post.objects.filter(Q(titulo__icontains = queryset) | Q(descripcion__icontains = queryset) | Q(contenido__icontains = queryset)).distinct()
        
        return render(request, 'blog.html', {'posts_blog':posts_blog, 'posts':posts})
    
    else:
        return render(request, 'detallepost.html', {'detallepost':post, 'posts':posts})
    