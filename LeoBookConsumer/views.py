from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.core.mail import send_mail
from ProjectDAW2do import settings
# Create your views here.


def index(request):
    if request.method == 'GET':
        glibros = requests.get('http://127.0.0.1:8000/')
        libros = glibros.json()
        context = {
            'libros': libros
        }
        return render(request, 'LeoBook/index.html', context)


def inicio(request):
    print("Hola")
    send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['jealvia@espol.edu.ec'],
        fail_silently=False,
    )
    print("hola2")
    return render(request, 'LeoBook/inicio.html')


def blog(request):
    return render(request, 'LeoBook/blog.html')


def chart(request):
    return render(request, 'LeoBook/chart.html')


def unete(request):
    return render(request, 'LeoBook/unete.html')


def nosotros(request):
    return render(request, 'LeoBook/nosotros.html')


def toplibros(request):
    return render(request, 'LeoBook/toplibros.html')
