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
from .serializers import *
from .models import *
import random as rd
import time
from datetime import datetime
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
    
class book_id(APIView):
    def get(self, request,id):
        libro = Libro.objects.get(pk=id)
        serializer = LibroSerializer(libro,many=False)
        return JsonResponse(serializer.data, safe = False)

class reservar_id(APIView):
    def get(self, request,id):
        reserva = Reserva.objects.filter(id_usuario=id)
        reservas = ReservaSerializer(reserva,many=True)
        return JsonResponse(reservas.data, safe = False)
        

class user_login(APIView):
    def get(self, request):
        try:
            print(request.POST['correo'])
            usuario=Usuario.objects.get(correo=request.POST['correo'])
            print(usuario.nombres)
        except:
            return JsonResponse({'validacion':False},status=400)
        if(usuario.password==request.POST['password']):
            print("se fue")
            serializer = UsuarioSerializer(usuario,many=False)
            return JsonResponse(serializer.data, safe = False)
        else:
            return JsonResponse({'validacion':False},status=400)

class user_id(APIView):
    def get(self, request,id):
        usuario = get_object_or_404(Usuario, pk= id)
        serializer = UsuarioSerializer(usuario,many=False)
        return JsonResponse(serializer.data,safe = False)

class registro_id(APIView):
    def get(self, request,id):
        registro = Registro_Ventas.objects.filter(id_usuario=id)
        serializer = RegistroVentasSerializer(registro,many=True)
        return JsonResponse(serializer.data, safe = False)

class registro_list(APIView):
    def get(self, request):
        registro = Registro_Ventas.objects.all()
        serializer = RegistroVentasSerializer(registro,many=True)
        return JsonResponse(serializer.data, safe = False)

class descripcion_venta_id(APIView):
    def get(self, request,id):
        descripcion = Descripcion_Venta.objects.get(id=id)
        serializer = DescripcionVentasSerializer(descripcion,many=False)
        return JsonResponse(serializer.data, safe = False)

class descripcion_venta_list(APIView):
    def get(self, request):
        descripcion = Descripcion_Venta.objects.all()
        serializer = DescripcionVentasSerializer(descripcion,many=True)
        return JsonResponse(serializer.data, safe = False)

class eliminar_reserva(APIView):
    def get(self, request,id):
        try:
            reserva=Reserva.objects.get(id=id)
        except:
            return JsonResponse({'validacion':False},status=400)
        reserva.delete()
        return JsonResponse({'validacion':True},status=200)

class actualizar_reserva(APIView):
    def post(self, request, id):
        try:
            reserva=Reserva.objects.get(id=id)
        except:
            return JsonResponse({'validacion':False},status=400)
        reserva.cantidad=request.POST['cantidad']
        reserva.save()
        if reserva.cantidad == request.POST['cantidad']:
            print("si es igual")
            return JsonResponse({'validacion': True}, status=200)
        return JsonResponse({'validacion': False}, status=400)

class book_sell(APIView):
    def post(self, request, user,book):
        usuario=get_object_or_404(Usuario, id=user)
        libro=get_object_or_404(Libro,id=book)
        datos={'cantidad':request.POST['cantidad'],'id_libro':[str(book)]}
        descripcion = DescripcionVentasSerializer(data=datos)
        
        if descripcion.is_valid():
            descripcion.save()
            print(descripcion)
            descrp = Descripcion_Venta.objects.latest('id')
            datos2={'total':int(request.POST['cantidad'])*int(libro.precio),'id_usuario':[str(usuario.id)],'id_descripcion_venta':[descrp.id]}
            serializer2=RegistroVentasSerializer(data=datos2)
            if serializer2.is_valid():
                serializer2.save()
                return JsonResponse(serializer2.data, status=201)
            else:
                return JsonResponse(serializer2.errors, status=400)
        return JsonResponse(descripcion.errors, status=400)

class book_reserve(APIView):
    @csrf_exempt
    def post(self, request,user,book):
        datos={'cantidad':request.POST['cantidad'],'estado': True,'id_libro':[str(book)],'id_usuario':[str(user)]}
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
        ,'id_libro_fav':[request.POST['id_libro_fav']],'id_autor_fav':[request.POST['id_autor_fav']]}
        serializer = UsuarioSerializer(data=datos)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class user_update(APIView):
    def post(self, request, user):
        usuario = get_object_or_404(Usuario, id=user)
        usuario.nombres=request.POST['nombre']
        usuario.correo=request.POST['correo']
        usuario.password=request.POST['password']
        print("es una prueba"+str(request.POST['id_libro_fav']))
        if request.POST['id_libro_fav'] != "nada":
            usuario.id_libro_fav.add(request.POST['id_libro_fav'])
        if request.POST['id_autor_fav'] != "nada":
            usuario.id_autor_fav.add(request.POST['id_autor_fav'])
        usuario.save()
        return JsonResponse({'validacion': True}, status=200)

class user_delete(APIView):
    def get(self, request, user):
        try:
            usuario=Usuario.objects.get(id=user)
        except:
            return JsonResponse({'validacion':False},status=400)
        usuario.delete()
        return JsonResponse({'validacion':True},status=200)

class blog_list(APIView):
    @csrf_exempt
    def get(self, request):
        print("Entro al blog")
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
    def get(self, request):
        evento = Contenido_Evento.objects.all()
        serializer = EventoSerializer(evento,many=True)
        return JsonResponse(serializer.data, safe = False)

class event_id(APIView):
    def get(self, request,event_id):
        evento = get_object_or_404(Contenido_Evento,pk=event_id)
        serializer = EventoSerializer(evento)
        return JsonResponse(serializer.data, safe = False)

class validar_login(APIView):
    def get(self,request):
        try:
            print(request.POST)
            print(request.POST['usuario'])
            admin=Administrador.objects.get(usuario=request.POST['usuario'])
        except:
            return JsonResponse({'validacion':False},status=400)
        print("Hola fueraa")
        if(admin.contrasena==request.POST['contrasena']):
            return JsonResponse({'validacion':True},status=200)


class blog_create(APIView):
    def post(self, request):
        print("Hola")
        print(request.POST['fecha'])
        print()
        temp_date = datetime.strptime(request.POST['fecha'], "%Y-%m-%d").date()
        datos = {'titulo': request.POST['titulo'], 'contenido': request.POST['contenido'],
                 'autor': request.POST['autor']
            , 'fecha': temp_date}
        serializer = BlogSerializer(data=datos)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class up_del_blog(APIView):
    def update(self,request,blog):
        blog = get_object_or_404(Contenido_Blog, id=blog)
        blog.titulo = request.POST['titulo']
        blog.contenido = request.POST['contenido']
        blog.autor = request.POST['autor']
        blog.fecha= request.POST['fecha']
        blog.save()
        return JsonResponse({'validacion': True}, status=200)
    def delete(self, request,blog):
        try:
            blog=Contenido_Blog.objects.get(id=blog)
        except:
            return JsonResponse({'validacion':False},status=400)
        blog.delete()
        return JsonResponse({'validacion':True},status=200)

def chart(request):
    return render(request,'LeoBook/chart.html',{'Libros':Libro.objects.all(),'Registro':Registro_Ventas.objects.all(),'Descripcion':Descripcion_Venta.objects.all(),'Usuario':Usuario.objects.all()})
