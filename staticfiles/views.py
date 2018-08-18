from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'LeoBook/index.html')

def inicio(request):
    return render(request,'LeoBook/inicio.html')

def blog(request):
    return render(request,'LeoBook/blog.html')

def chart(request):
    return render(request,'LeoBook/chart.html')

def unete(request):
    return render(request,'LeoBook/unete.html')

def nosotros(request):
    return render(request,'LeoBook/nosotros.html')

def toplibros(request):
    return render(request,'LeoBook/toplibros.html')