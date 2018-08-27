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
    if request.method == 'GET':
        booklist = requests.get('http://127.0.0.1:8000/book/')
        books = booklist.json()
        import os
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'templates\\LeoBook\\mycsv.csv')
        d={}
        print(books)
        for elem in books:
            l1=[]
            l2=[]
            for aut in elem['id_autor']:
                lis_aut=requests.get('http://127.0.0.1:8000/author/')
                lis_aut=lis_aut.json()
                for a in lis_aut:
                    if a['id']==aut:
                        l1.append(a['nombre'])        
            for cc in elem['id_categoria']:
                lis_cat=requests.get('http://127.0.0.1:8000/category/')
                lis_cat=lis_cat.json()
                for c in lis_cat:
                    if c['id']==cc:
                        l2.append(c['nombre']) 
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
                    f.write("LeoBook|"+str(el) + "|" + str(elemento)+"|"+str(nin['nombre']) + "," + str(rd.randint(100, 1500)) + ",\n")
        f.close()
        context = {
            'books' : books
        }
        return render(request, 'LeoBook/index.html', context)


def indexUser(request):
    if request.method == 'GET':
        booklist= requests.get('http://127.0.0.1:8000/book/')
        books = booklist.json()
        import os
        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'templates\\LeoBook\\mycsv.csv')
        d={}
        print(books)
        for elem in books:
            l1=[]
            l2=[]
            for aut in elem['id_autor']:
                lis_aut=requests.get('http://127.0.0.1:8000/author/')
                lis_aut=lis_aut.json()
                for a in lis_aut:
                    if a['id']==aut:
                        l1.append(a['nombre'])        
            for cc in elem['id_categoria']:
                lis_cat=requests.get('http://127.0.0.1:8000/category/')
                lis_cat=lis_cat.json()
                for c in lis_cat:
                    if c['id']==cc:
                        l2.append(c['nombre']) 
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
                    f.write("LeoBook|"+str(el) + "|" + str(elemento)+"|"+str(nin['nombre']) + "," + str(rd.randint(100, 1500)) + ",\n")
        f.close()
        context = {
            'nombre' : request.session['user_name'],
            'id': request.session['user_id'],
            'books' : books
        }
        return render(request, 'LeoBook/indexUser.html', context)


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
        user = respuesta.json()
        if respuesta.status_code == 400:
            return redirect('login')
        else:
            request.session['user_name'] = user['nombres']
            request.session['user_id'] = user['id']
            booklist= requests.get('http://127.0.0.1:8000/book/')
            books = booklist.json()
            context = {
                'nombre' : request.session['user_name'],
                'id': request.session['user_id'],
                'books' : books
            }
            response = render(request,'LeoBook/indexUser.html',context)
            return response
            


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
        user = requests.post('http://127.0.0.1:8000/user_register/', data = {'nombre' : request.POST['nombre'],'image' : request.POST['image'], 'correo' : request.POST['correo'],'password' : request.POST["password"],'id_libro_fav' : request.POST["id_libro_fav"],'id_autor_fav' : request.POST["id_autor_fav"]})
        return render(request,'LeoBook/inicio.html')

def blog(request):
    blog_list = requests.get('http://127.0.0.1:8000/blog/')
    blogs = blog_list.json()
    context = {
        'blogs' : blogs
    }
    return render(request, 'LeoBook/blog.html',context)

def blogUser(request):
    blog_list = requests.get('http://127.0.0.1:8000/blog/')
    blogs = blog_list.json()
    context = {
        'nombre' : request.session['user_name'],
        'id': request.session['user_id'],
        'blogs' : blogs
    }
    return render(request, 'LeoBook/blogUser.html',context)

def events(request):
    event_list = requests.get('http://127.0.0.1:8000/events/')
    events = event_list.json()
    context = {
        'events' : events
    }
    return render(request, 'LeoBook/events.html',context)

def eventsUser(request):
    event_list = requests.get('http://127.0.0.1:8000/events/')
    events = event_list.json()
    context = {
        'events' : events,
        'nombre' : request.session['user_name'],
        'id': request.session['user_id']
    }
    return render(request, 'LeoBook/eventsUser.html',context)

def csv(request):
    return render(request,'LeoBook/mycsv.csv')
def chart(request):
    booklist = requests.get('http://127.0.0.1:8000/book/')
    authorlist = requests.get('http://127.0.0.1:8000/author/')
    books = booklist.json()
    authors = authorlist.json()
    reglist = requests.get('http://127.0.0.1:8000/register/')
    salelist = requests.get('http://127.0.0.1:8000/description_sale/')
    reg = reglist.json()
    sale = salelist.json()
    return render(request, 'LeoBook/chart.html',{'Libros':books,'Registro':reg,'Descripcion':sale})


def unete(request):
    return render(request, 'LeoBook/unete.html')


def nosotros(request):
    return render(request, 'LeoBook/nosotros.html')

def nosotrosUser(request):
    context = {
        'nombre' : request.session['user_name'],
        'id': request.session['user_id'],
    }
    return render(request, 'LeoBook/nosotrosUser.html',context)


def toplibros(request):
    return render(request, 'LeoBook/toplibros.html')

def toplibrosUser(request):
    context = {
        'nombre' : request.session['user_name'],
        'id': request.session['user_id'],
    }
    return render(request, 'LeoBook/toplibrosUser.html',context)

def comprar(request,id):
    id_book = id
    response = render(request,'LeoBook/inicio.html')
    response.set_cookie('id_book', id_book)
    return response

def reservar(request,id):
    id_book = id
    response = render(request,'LeoBook/inicio.html')
    response.set_cookie('id_book', id_book)
    return response

@csrf_exempt 
def comprarUser(request,id_book,id_user):
    if request.method == "POST":
        id_book = id_book
        id_book = id_user
        greserva = requests.post('http://127.0.0.1:8000/booksell/'+str(id_user)+"/"+str(id_book)+"/", data={'cantidad' : request.POST['cantidad']})
        context = {
            'nombre' : request.session['user_name'],
            'id': request.session['user_id'],
        }
        return render(request,'LeoBook/userCompras.html',context)

@csrf_exempt 
def reservarUser(request,id_book,id_user):
    if request.method == "POST":
        id_book = id_book
        id_book = id_user
        sreserva = requests.post('http://127.0.0.1:8000/user_reserve/'+str(id_user)+"/"+str(id_book)+"/", data={'cantidad' : request.POST['cantidad']})
        greserva = requests.get('http://127.0.0.1:8000/reservar/'+str(id_user)+"/")
        reservas = greserva.json()
        context = {
            'nombre' : request.session['user_name'],
            'id': request.session['user_id'],
            'reservas' : reservas
        }
        return render(request,'LeoBook/userReservas.html',context)

def misreservas(request, user):
    greserva = requests.get('http://127.0.0.1:8000/reservar/'+str(user)+"/")
    reservas = greserva.json()
    context = {
        'nombre' : request.session['user_name'],
        'id': request.session['user_id'],
        'reservas' : reservas
    }
    return render(request,'LeoBook/userReservas.html',context)