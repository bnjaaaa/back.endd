from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>soy el index de la app3</h1><p>Nelson</p><a href="http://127.0.0.1:8000/">volver a la pagina 404</a>')