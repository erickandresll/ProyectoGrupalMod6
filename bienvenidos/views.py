from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bienvenido(request):
    return HttpResponse("Bienvenidos a Te lo vendo")

