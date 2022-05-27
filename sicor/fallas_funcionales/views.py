from django.shortcuts import render
from .models import *
from .forms import FormularioTipoEquipo,FormularioCalificacionFalla,FormularioFalla
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.core import serializers

# Create your views here.
#LISTAR TIPOS DE EQUIPO///////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////
class listarTiposEquipos(ListView):
    model= TipoDeEquipo
    template_name='fallas_equipo_muestra.html'
    context_object_name='equipos'
    paginate_by=20
    ordering = ['nombre']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeEquipo.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class listarFallas(ListView):
    model= Falla
    template_name='fallas_muestra.html'
    context_object_name='fallas'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Falla.objects.filter(
                Q(descripcion__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()
        
class listarCalificacionFallas(ListView):
    model= CalificacionFalla
    template_name='fallas_calificacion_muestra.html'
    context_object_name='calificaciones'
    paginate_by=20
    ordering = ['descripcion']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Falla.objects.filter(
                Q(descripcion__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()   

#///////////////////////////////////////////////////////////////////////////////////////////////
#FORMULARIOS ////////////////////////////////////////////////////////////////////////////////////
class formularioFalla(CreateView):    
    model=Falla
    form_class=FormularioFalla                     #FALLAS FUNCIONALES
    template_name="fallas_FormFalla.html"
    success_url=reverse_lazy("fallas_muestra")

class formularioCalificaionFalla(CreateView):    
    model=CalificacionFalla
    form_class=FormularioCalificacionFalla                     #CALIFICACIÓN FALLA
    template_name="fallas_FormCalificacionFalla.html"
    success_url=reverse_lazy("fallas_calificacion_muestra")

class formularioTipoEquipo(CreateView):    
    model=TipoDeEquipo
    form_class=FormularioTipoEquipo                     #TIPOS DE EQUIPO
    template_name="fallas_FormTipodeEquipo.html"
    success_url=reverse_lazy("fallas_equipo_muestra")

#INFORMACIÓN DE FILTRADO//////////////////////////////////////////////////////////////////

def vista_listado_tipos(request):
    lista=TipoDeEquipo.objects.all()  # asignar valores desde los modelos a la variable lista
    lista2=Falla.objects.all()  # asignar valores desde los modelos a la variable lista

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    posts_serialized2 = serializers.serialize('json', lista2) # se da formato json a la lista de archivos

    return JsonResponse({"listado":posts_serialized,"listado2":posts_serialized2}) # regresa la informacion en formato json

#//////////////////////////////////////////////////////////////////////////////////////////////////////
#EDITAR Y ELIMINAR ELEMENTOS////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////

#FALLAS FUNCIONALES

class listafallas_editar(UpdateView):
    model=Falla
    form_class=FormularioFalla
    template_name="fallas_FormFalla.html"
    success_url=reverse_lazy("fallas_muestra")

class listafallas_eliminar(DeleteView):
    model=Falla
    template_name="fallas_eliminar.html"
    success_url=reverse_lazy("fallas_muestra")

#CALIFICACIÓN DE FALLA

class listacalificacionfallas_editar(UpdateView):
    model=CalificacionFalla
    form_class=FormularioCalificacionFalla
    template_name="fallas_FormCalificacionFalla.html"
    success_url=reverse_lazy("fallas_calificacion_muestra")

class listacalificacionfallas_eliminar(DeleteView):
    model=CalificacionFalla
    template_name="fallas_calificacion_eliminar.html"
    success_url=reverse_lazy("fallas_calificacion_muestra")

#TIPOS DE EQUIPOS

class listatipoequipo_editar(UpdateView):
    model=TipoDeEquipo
    form_class=FormularioTipoEquipo
    template_name="fallas_FormTipodeEquipo.html"
    success_url=reverse_lazy("fallas_equipo_muestra")

class listatipoequipo_eliminar(DeleteView):
    model=TipoDeEquipo
    template_name="fallas_tipoequipo_eliminar.html"
    success_url=reverse_lazy("fallas_equipo_muestra")

