from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.core.mail import send_mail
from ProjectDAW2do import settings
from LeoBookAPI.models import *
import random as rd
# Create your views here.


def index(request):
    import os
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'templates\\LeoBook\\mycsv.csv')
    lib=Libro.objects.all()
    d={}
    for elem in lib:
        l1=[]
        l2=[]
        for aut in elem.id_autor.all():
            l1.append(aut.nombre)
        for cc in elem.id_categoria.all():
            l2.append(cc.nombre)
        _aut=",".join(l1)
        _cat=",".join(l2)
        if _aut not in d:
            d[_aut]={_cat:[elem]}
        else:
            if _cat not in d[_aut]:
                d[_aut][_cat]=[elem]
            else:
                d[_aut][_cat].append(elem)
    f=open(filename,"w",encoding="utf-8")
    f.write("id,value\n")
    f.write("LeoBook,\n")
    for el in d:
        f.write("LeoBook|"+str(el)+",\n")
        for elemento in d[el]:
            f.write("LeoBook|"+str(el)+"|"+str(elemento)+",\n")
            for nin in d[el][elemento]:
                f.write("LeoBook|"+str(el) + "|" + str(elemento)+"|"+nin.nombre + "," + str(rd.randint(100, 1500)) + ",\n")
    f.close()
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

@csrf_exempt 
def authenticate(request):
    if request.method == "POST":
        respuesta = requests.get('http://127.0.0.1:8000/login/', data = {'correo' : request.POST['correo'], 'password' : request.POST["password"]})
        login = respuesta.json()
        print(login)
        if login['validacion'] == True:
            return render(request,'LeoBook/dashboard.html')
        else:
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

def csv(request):
    return render(request,'LeoBook/mycsv.csv')
def chart(request):
    return render(request, 'LeoBook/chart.html',{'Libros':Libro.objects.all(),'Registro':Registro_Ventas.objects.all(),'Descripcion':Descripcion_Venta.objects.all(),'Usuario':Usuario.objects.all()})


def unete(request):
    return render(request, 'LeoBook/unete.html')


def nosotros(request):
    return render(request, 'LeoBook/nosotros.html')


def toplibros(request):
    return render(request, 'LeoBook/toplibros.html')
