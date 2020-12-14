from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from blog.models import Post
from django.http import HttpResponse

def home(request):
    
    """ Queryset de la home mostrando los ultimos 6 posts """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:6]

    return render(request, "home.html", {'posts':posts})

def contact(request):
    
    """ Queryset de la home mostrando los ultimos 6 posts """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:3]
    
    if request.method == "POST":
        your_name = request.POST["message-name"]
        message_phone = request.POST["message-phone"]
        message = request.POST["message"]
        email_from = "¡Nueva consulta desde tu página web! <dr.rossi.ceo@gmail.com>"
        recipient_list = ['jr.ceo@hotmail.com.ar',]
      
        #sending email
        send_mail(
            'Email de: ' + your_name, #subject, in this case, the name
            message + '\n \n' + 'Número de teléfono para contactar: ' + message_phone, #message
            email_from, #from email
            recipient_list
        )
        
        return render(request, "appointment.html", {'your_name':your_name, 'posts':posts})

        
        
    else:
        return render(request, "contact.html")


def about(request):
    
    """ Queryset de la home mostrando los ultimos 6 posts """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:3]
    
    return render(request, "about.html",  {'posts':posts})

def service(request):
    
    """ Queryset de la home mostrando los ultimos 6 posts """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:3]
    
    return render(request, "service.html", {'posts':posts})



def appointment(request):
    
    """ Queryset de la home mostrando los ultimos 6 posts """
    posts = Post.objects.filter(publicado=True).order_by('-id')[:3]
    
    if request.method == "POST":
        your_name = request.POST["your-name"]
        your_phone = request.POST["your-phone"]
        your_message = request.POST["your-message"]
        email_from = "¡Nueva consulta desde tu página web! <dr.rossi.ceo@gmail.com>"
        recipient_list = ['jr.ceo@hotmail.com.ar',]
      
        #sending email
        send_mail(
            'Consulta de: ' + your_name, #subject, in this case, the name
            your_message + '\n \n' + 'Número de teléfono para contactar: ' + your_phone, #message
            email_from, #from email
            recipient_list
        )
        
        return render(request, "appointment.html", {'your_name':your_name, 'posts':posts})

        
    else:
        return render(request, "404.html")
    
    
    
def error_404(request, exception):
    return render(request, "404.html")
    