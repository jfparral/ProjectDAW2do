from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
import random as rd
#Mias
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status 
from rest_framework.response import Response 
from rest_framework.views import APIView 
from django.http import Http404,JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    lib=Libro.objects.all()
    libros = LibroSerializer(lib,many=True)
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
    f.write("id,value\n")
    for el in d:
        f.write(el.nombre+",\n")
        for elemento in d[el]:
            f.write(el.nombre+"."+elemento.nombre+",\n")
            for nin in d[el][elemento]:
                f.write(el.nombre + "." + elemento.nombre+"."+nin.nombre + "," + str(rd.randint(100, 3500)) + ",\n")
    f.close()

    return JsonResponse(libros.data)

class author_list(APIView):
    def get(self, request):
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores,many=True)
        return JsonResponse(serializer.data, safe = False)

class category_list(APIView):
    def get(self, request):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria,many=True)
        return JsonResponse(serializer.data, safe = False)

class book_list(APIView):
    def get(self, request):
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros,many=True)
        return JsonResponse(serializer.data, safe = False)

class user_login(APIView):
    def get(self, request):
        try:
            print(request.POST['correo'])
            usuario=Usuario.objects.get(correo=request.POST['correo'])
        except:
            return JsonResponse({'validacion':False},status=400)
        if(usuario.password==request.POST['password']):
            return JsonResponse({'validacion':True}, safe = False)
        else:
            return JsonResponse({'validacion':False},status=400)

class registro_list(APIView):
    def get(self, request):
        registro = Registro_Ventas.objects.all()
        serializer = RegistroVentasSerializer(registro,many=True)
        return JsonResponse(serializer.data, safe = False)

class descripcion_venta_list(APIView):
    def get(self, request):
        descripcion = Descripcion_Venta.objects.all()
        serializer = DescripcionVentasSerializer(descripcion,many=True)
        return JsonResponse(serializer.data, safe = False)

class book_sell(APIView):
    def post(self, request, user,book):
        usuario=get_object_or_404(Usuario, id=user)
        libro=get_object_or_404(Libro,id=book)
        datos={'cantidad':request.POST['cantidad'],'id_libro':[str(book)]}
        serializer = DescripcionVentasSerializer(data=datos)
        print(serializer)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            venta=Descripcion_Venta.objects.all()
            #Aqui puedde haber error con el len venta
            datos2={'total':int(request.POST['cantidad'])*libro.precio,'id_usuario':[str(usuario.id)],'id_descripcion_venta':[str(len(venta))]}
            serializer2=RegistroVentasSerializer(data=datos2)
            if serializer2.is_valid():
                serializer2.save()
                return JsonResponse(serializer2.data, status=201)
            else:
                return JsonResponse(serializer.errors, status=400)
        return JsonResponse(serializer.errors, status=400)

class book_reserve(APIView):
    @csrf_exempt
    def post(self, request,user,book):
        datos={'cantidad':request.POST['cantidad'],'estado':request.POST['estado'],'id_libro':[str(book)],'id_usuario':[str(user)]}
        serializer = ReservaSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, safe = False)

class user_detail_compras(APIView):
    @csrf_exempt
    def get(self, request,user):
        compra=Registro_Ventas.objects.get(id_usuario=user)
        serializer = RegistroVentasSerializer(compra,many=True)
        return JsonResponse(serializer.data, safe = False)

class crear(APIView):
    def post(self, request):
        datos={'nombres':request.POST['nombre'],'correo':request.POST['correo'],'password':request.POST['password']
        ,'id_libro_fav':[request.POST['id_libro_fav']],'id_autor_fav':[request.POST['id_autor_fav']],'image' : request.FILES['image'].file}
        serializer = UsuarioSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class user_update(APIView):
    def post(self, request, user):
        usuario = get_object_or_404(Usuario, pk=user)
        usuario.nombres=request.POST['nombres']
        usuario.correo=request.POST['correo']
        usuario.password=request.POST['password']
        usuario.id_libro_fav=request.POST['id_libro_fav']
        usuario.id_autor_fav=request.POST['id_autor_fav']
        usuario.save()
        serializer = UsuarioSerializer(usuario)
        if not serializer.is_valid():
            return HttpResponse(status=404)
        serializer.save()
        return JsonResponse(serializer.data)

class user_delete(APIView):
    def post(self, request, user):
        usuario = get_object_or_404(Usuario, pk=user)
        usuario.delete()
        return HttpResponse(status=204)

class blog_list(APIView):
    @csrf_exempt
    def get(self, request):
        blogs = Contenido_Blog.objects.all()
        serializer = BlogSerializer(blogs,many=True)
        return JsonResponse(serializer.data, safe = False)

class blog_id(APIView):
    @csrf_exempt
    def get(self, request,blog_id):
        blogs = get_object_or_404(Contenido_Blog,pk=blog_id)
        serializer = BlogSerializer(blogs)
        return JsonResponse(serializer.data, safe = False)

class event_list(APIView):
    @csrf_exempt
    def get(self, request):
        evento = Contenido_Evento.objects.all()
        serializer = EventoSerializer(evento,many=True)
        return JsonResponse(serializer.data, safe = False)

class event_id(APIView):
    @csrf_exempt
    def get(self, request,event_id):
        evento = get_object_or_404(Contenido_Evento,pk=event_id)
        serializer = EventoSerializer(evento)
        return JsonResponse(serializer.data, safe = False)



def chart(request):
    return render(request,'LeoBook/chart.html',{'Libros':Libro.objects.all(),'Registro':Registro_Ventas.objects.all(),'Descripcion':Descripcion_Venta.objects.all(),'Usuario':Usuario.objects.all()})


