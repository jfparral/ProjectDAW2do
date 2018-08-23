from django.shortcuts import render,redirect
from LeoBook.models import *
from LeoBook.serializers import *
from rest_framework import generics
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

class EventoListar(APIView):
    @csrf_exempt
    def get(self, request):
        evento = Contenido_Evento.objects.all()
        serializer = EventoSerializer(evento,many=True)
        return JsonResponse(serializer.data, safe = False)