from django.shortcuts import render

from django.http import HttpResponse
from django.template import Template, Context, loader
from Familia.models import Familiares
# Create your views here.

def listar(request):
    queryset = Familiares.objects.all()
    diccionario = {"Familia" : queryset}
    plantilla = loader.get_template("Familia_list.html")
    documento_html = plantilla.render(diccionario)
    return HttpResponse(documento_html)

