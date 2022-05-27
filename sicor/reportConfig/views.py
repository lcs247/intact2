from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import ConfiguracionReporte
from .forms import FormularioConfigReporte
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# Create your views here.

class formularioConfigReporte(CreateView):    
    model=ConfiguracionReporte
    form_class=FormularioConfigReporte                     #FORMULARIO DE CONFIGURACIONES DE PDF
    template_name="reporte_config_form.html"
    success_url=reverse_lazy("inicio")

class listarConfig(ListView):
    model= ConfiguracionReporte
    template_name='inicio.html'
    context_object_name='configs'

class editar_formConfigReporte(UpdateView):
    model=ConfiguracionReporte
    form_class=FormularioConfigReporte                     #EDITAR CONFIGURACIONES DE PDF
    template_name="reporte_config_form.html"
    success_url=reverse_lazy("inicio")

def vista_listado_configReport(request):
    lista=ConfiguracionReporte.objects.all()  # asignar valores desde los modelos a la variable lista
    #lista2=EquipoPrincipal.objects.all()
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    #posts_serialized2 = serializers.serialize('json', lista2)
    context={"listado":posts_serialized}

    return JsonResponse(context) # regresa la informacion en formato json
