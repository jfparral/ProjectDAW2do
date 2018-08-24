from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    cat=Categoria.objects.all()
    lib=Libro.objects.all()
    aut=Autor.objects.all()
    d={}
for elem in lib:
    _aut=elem.id_autor
    _cat=elem.id_categoria
    if _aut not in d:
        d[_aut]={_cat:[elem]}
    else:
        if _cat not in d[_aut]:
            d[_aut][_cat]=[elem]
        else:
            d[_aut][_cat].append(elem)
f=open("mycsv.csv","w")
import random as rd
f.write("id,value\n")
for el in d:
    f.write(el+",\n")
    for elemento in d[el]:
        f.write(el+"."+elemento+",\n")
        for nin in d[el][elemento]:
            f.write(el + "." + elemento+"."+nin + "," + str(rd.randint(100, 3500)) + ",\n")
f.close()

    return render(request,'LeoBook/index.html')

def inicio(request):
    return render(request,'LeoBook/inicio.html')

def blog(request):
    return render(request,'LeoBook/blog.html')

def chart(request):
    return render(request,'LeoBook/chart.html',{'Libros':Libro.objects.all(),'Registro':Registro_Ventas.objects.all(),'Descripcion':Descripcion_Venta.objects.all(),'Usuario':Usuario.objects.all()})

def unete(request):
    return render(request,'LeoBook/unete.html')

def nosotros(request):
    return render(request,'LeoBook/nosotros.html')

def toplibros(request):
    return render(request,'LeoBook/toplibros.html')
