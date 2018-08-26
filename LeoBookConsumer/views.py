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
        booklist= requests.get('http://127.0.0.1:8000/book/')
        books = booklist.json()
        context = {
            'books' : books
        }
        return render(request, 'LeoBook/index.html', context)


def login(request):
    """ send_mail(
        'Subject here',
        'Here is the message.',
        settings.EMAIL_HOST_USER,
        ['jealvia@espol.edu.ec'],
        fail_silently=False,
    ) """
    return render(request,'LeoBook/inicio.html')

def register(request):
    booklist = requests.get('http://127.0.0.1:8000/book/')
    authorlist = requests.get('http://127.0.0.1:8000/author/')
    books = booklist.json()
    authors = authorlist.json()
    context = {
        'books' : books,
        'authors' : authors
    }
    return render(request,'LeoBook/registro.html',context)

@csrf_exempt 
def sendRegister(request):
    if request.method == "POST":
        user = requests.post('http://127.0.0.1:8000/user_register/', data = {'nombre' : request.POST['nombre'],'correo' : request.POST['correo'],'password' : request.POST["password"],'id_libro_fav' : request.POST["id_libro_fav"],'id_autor_fav' : request.POST["id_autor_fav"]})
        return render(request,'LeoBook/inicio.html')

def blog(request):
    blog_list = requests.get('http://127.0.0.1:8000/blog/')
    blogs = blog_list.json()
    context = {
        'blogs' : blogs
    }
    return render(request, 'LeoBook/blog.html',context)


def chart(request):
    return render(request, 'LeoBook/chart.html')


def unete(request):
    return render(request, 'LeoBook/unete.html')


def nosotros(request):
    return render(request, 'LeoBook/nosotros.html')


def toplibros(request):
    return render(request, 'LeoBook/toplibros.html')
