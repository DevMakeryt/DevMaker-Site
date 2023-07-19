from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def retornar_frase(request):
    frase = "Esta é a frase que será retornada pela URL do Django!"
    return HttpResponse(frase)