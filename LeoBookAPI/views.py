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
import json
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
    def patch(self,request,blog):
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

#Eventos
class manage_events(APIView):
    def get(self,request):
        eventos=Contenido_Evento.objects.all()
        serializer=EventoSerializer(eventos,many=True)
        return JsonResponse(serializer.data, safe=False)
    def post(self, request):
        print("Hola")
        print(request.POST['fecha'])
        print()
        temp_date = datetime.strptime(request.POST['fecha'], "%Y-%m-%d").date()
        datos = {'titulo': request.POST['titulo'], 'contenido': request.POST['contenido']
            , 'fecha': temp_date}
        serializer = EventoSerializer(data=datos)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class upd_rem_evento(APIView):
    def patch(self, request, even):
        evento = get_object_or_404(Contenido_Evento, id=even)
        evento.titulo = request.POST['titulo']
        evento.contenido = request.POST['contenido']
        evento.fecha = request.POST['fecha']
        evento.save()
        return JsonResponse({'validacion': True}, status=200)
    def delete(self, request, even):
        try:
            evento = Contenido_Evento.objects.get(id=even)
        except:
            return JsonResponse({'validacion': False}, status=400)
        evento.delete()
        return JsonResponse({'validacion': True}, status=200)

# Reportes
class obtener_usuarios(APIView):
    def get(self):
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, many=True)
        return JsonResponse(serializer, status=200)

class reportes_usuarios(APIView):
    def get(self, request, id):
        ventas = Registro_Ventas.objects.filter(id_usuario=id)
        datos = "{"
        for venta in ventas:
            datos += "{'" + venta.id + "':" + "{" + "'usuario'" + ":" + venta.id_usuario.get().nombres + "," + \
                     "'libro':" + venta.id_descripcion_venta.get().id_libro.get().nombre + "," + \
                     "'cantidad':" + venta.id_descripcion_venta.get().cantidad + "," + "'total':" + venta.total + "}}"
        datos += "}"
        json_dat = json.loads(datos)
        return JsonResponse(json_dat, status=200)

class reportes(APIView):
    def get(self, request):
        ventas = Registro_Ventas.objects.all()
        datos = {}
        for venta in ventas:
            datos[venta.id]={}
            datos[venta.id]['id']=venta.id
            datos[venta.id]['usuario']=venta.id_usuario.get().nombres
            datos[venta.id]['libro']=venta.id_descripcion_venta.get().id_libro.get().nombre
            datos[venta.id]['cantidad']=venta.id_descripcion_venta.get().cantidad
            datos[venta.id]['total']=venta.total
        return JsonResponse(datos, status=200)
    def post(self, request):
        print("usuario,libro,cantidad,total")
        if (request.POST['usuario'] == "" or request.POST['cantidad'] == "" or request.POST['libro'] == "" or
                request.POST['total'] == ""):
            return JsonResponse({'validacion': False}, status=400)
        else:
            reporte = Reportes(usuario=request.POST['usuario'], libro=request.POST['libro'],
                               cantidad=request.POST['cantidad'], total=request.POST['total'])
            reporte.save(using='default')
            return JsonResponse({'validacion': True}, status=200)

class chart_descripcion(APIView):
    def get(self,request):
        descripcion=Descripcion_Venta.objects.all()
        datos={}
        for desc in descripcion:
            datos[desc.id]={}
            datos[desc.id]['id']=desc.id
            datos[desc.id]['cantidad']=desc.cantidad
            datos[desc.id]['libro']=desc.id_libro.get().nombre
        return JsonResponse(datos, status=200)

class chart_registro(APIView):
    def get(self, request):
        registro = Registro_Ventas.objects.all()
        datos = {}
        for desc in registro:
            datos[desc.id]={}# += '{"id":' + str(desc.id) + ',"total":' + str(desc.total) + ',"usuario":' + desc.id_usuario.get().nombres + '},'
            datos[desc.id]['id']=str(desc.id)
            datos[desc.id]['total']=str(desc.total)
            datos[desc.id]['usuario'] = str(desc.id_usuario.get().nombres)
        return JsonResponse(datos, status=200)

def chart(request):
    return render(request,'LeoBook/chart.html',{'Libros':Libro.objects.all(),'Registro':Registro_Ventas.objects.all(),'Descripcion':Descripcion_Venta.objects.all(),'Usuario':Usuario.objects.all()})
