from tkinter import E
from typing import OrderedDict
from django.contrib.messages.api import success,error
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import EquipoPrincipal, Planta,Sistema,Equipo,SubSistema,PlantaSecundaria
from .forms import FormularioPlanta,FormularioSistema,FormularioEquipo,FormularioEquipoPrincipal,FormularioPlantaSecundaria,FormularioSubSistema
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from fallas_funcionales.models import *

# Create your views here.
#FORMULARIOS
# def inicio(request):
#     return render (request,'inicio.html')

class formularioEquipoPrincipal(CreateView):    
    model=EquipoPrincipal
    form_class=FormularioEquipoPrincipal                     #EQUIPOS PRINCIPALES
    template_name="registro_equipos_principal.html"
    success_url=reverse_lazy("registro_muestra_Pr")

class formularioEquipo(CreateView):    
    model=Equipo
    form_class=FormularioEquipo                     #EQUIPOS SECUNDARIOS
    template_name="registro_equipos.html"
    success_url=reverse_lazy("registro_muestra")

class formularioSistema(CreateView):
    model=Sistema
    form_class=FormularioSistema                    #SISTEMA
    template_name="registro_sistema.html"
    success_url=reverse_lazy("listado_sistemas")

class formularioSubSistema(CreateView):
    model=SubSistema
    form_class=FormularioSubSistema
    template_name="registro_subsistema.html"            #SUBSITEMA
    success_url=reverse_lazy("listado_subsistemas")

class formularioPlanta(CreateView):
    model=Planta
    form_class=FormularioPlanta
    template_name="registro_planta.html"            #PLANTA PRINCIPAL
    success_url=reverse_lazy("listado_plantas")

class formularioPlantaSecundaria(CreateView):
    model=PlantaSecundaria
    form_class=FormularioPlantaSecundaria               #PLANTA SECUNDARIA
    template_name="registro_planta_secundaria.html"
    success_url=reverse_lazy("listado_plantas_Sec")

#PRESENTACIONES
# LISTADO DE EQUIPOS (PRINCIPAL Y SECUNDARIO)
# def listarEquipos(request):
#     queryset =request.GET.get("buscar")
#     equipo=Equipo.objects.all().order_by('planta')
#     equipo_pr=EquipoPrincipal.objects.all().order_by('planta')
#     if queryset:
#         equipo=Equipo.objects.filter(
#             Q(nombre__icontains = queryset) |
#             Q(codes__icontains = queryset) |
#             Q(codigo__icontains = queryset)).distinct()         #LISTAR Y FILTRAR EQUIPOS SECUNDARIOS Y PRINCIPALES

#         equipo_pr=EquipoPrincipal.objects.filter(
#             Q(nombre__icontains = queryset) |
#             Q(codigo__icontains = queryset) |
#             Q(codes__icontains = queryset)).distinct()
#     #print(equipo)
#     #print(equipo_pr)
#     contexto ={'equipos':equipo,'equiposs':equipo_pr}
#     return render(request,'registro_muestra.html',contexto)

class listarEquipos(ListView):
    model= Equipo
    template_name='registro_muestra.html'
    context_object_name='equipos'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Equipo.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar']) |
                Q(codes__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class listarEquiposPr(ListView):
    model= EquipoPrincipal
    template_name='registro_muestra.html'
    context_object_name='equiposs'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return EquipoPrincipal.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar']) |
                Q(codes__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class lista_editar(UpdateView):
    model=Equipo
    form_class=FormularioEquipo                     #EDITAR EQUIPO SECUNDARIO
    template_name="registro_equipos.html"
    success_url=reverse_lazy("registro_muestra")

class lista_editar_pr(UpdateView):
    model=EquipoPrincipal
    form_class=FormularioEquipoPrincipal               #EDITAR EQUIPO PRINCIPAL
    template_name="registro_equipos_principal.html"
    success_url=reverse_lazy("registro_muestra_Pr")

class lista_eliminar(DeleteView):
    model=Equipo
    template_name="registro_eliminar.html"          #ELIMINAR EQUIPO SECUNDARIO
    success_url=reverse_lazy("registro_muestra")

class lista_eliminar_pr(DeleteView):
    model=EquipoPrincipal
    template_name="registro_eliminar.html"          #ELIMINAR EQUIPO PRINCIPAL
    success_url=reverse_lazy("registro_muestra_Pr")

def vista_listado_activos(request):
    lista=Equipo.objects.all()  # asignar valores desde los modelos a la variable lista
    lista2=EquipoPrincipal.objects.all()
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    posts_serialized2 = serializers.serialize('json', lista2)
    return JsonResponse({"listado":posts_serialized,"listado2":posts_serialized2}) # regresa la informacion en formato json

# LISTADO DE PLANTAS (PRINCIPAL Y SECUNDARIA)

# def listarPlantas(request):
#     queryset =request.GET.get("buscar")
#     planta=Planta.objects.all().order_by('nombre')
#     planta_sec=PlantaSecundaria.objects.all().order_by('nombre')
#     if queryset:
#         planta=Planta.objects.filter(
#             Q(nombre__icontains = queryset) |
#             Q(codigo__icontains = queryset)).distinct()
    
#         planta_sec=PlantaSecundaria.objects.filter(             #LISTAR Y FILTRAR PLANTAS PRINCIPALES Y SECUNDARIAS
#             Q(nombre__icontains = queryset) |
#             Q(codigo__icontains = queryset)).distinct()
    
#     contexto ={'plantas':planta,'plantass':planta_sec}
#     return render(request,'listado_plantas.html',contexto) 

class listarPlantas(ListView):
    model= Planta
    template_name='listado_plantas.html'
    context_object_name='plantas'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Planta.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class listarPlantasSec(ListView):
    model= PlantaSecundaria
    template_name='listado_plantas.html'
    context_object_name='plantass'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return PlantaSecundaria.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()


class lista_p_editar(UpdateView):
    model=Planta
    form_class=FormularioPlanta                     #EDITAR PLANTA PRINCIPAL
    template_name="registro_planta.html"
    success_url=reverse_lazy("listado_plantas")

class lista_psec_editar(UpdateView):
    model=PlantaSecundaria          
    form_class=FormularioPlantaSecundaria               #EDITAR PLANTA SECUNDARIA
    template_name="registro_planta_secundaria.html"
    success_url=reverse_lazy("listado_plantas_Sec")

class lista_p_eliminar(DeleteView):
    model=Planta
    template_name="listado_plantas_eliminar.html"       #ELIMINAR PLANTA PRINCIPAL
    success_url=reverse_lazy("listado_plantas")

class lista_psec_eliminar(DeleteView):
    model=PlantaSecundaria
    template_name="listado_plantas_eliminar.html"        #ELIMINAR PLANTA SECUNDARIA
    success_url=reverse_lazy("listado_plantas_Sec")

def vista_listado_plantas(request):
    lista=Planta.objects.all()  # asignar valores desde los modelos a la variable lista
    lista2=PlantaSecundaria.objects.all()  # asignar valores desde los modelos a la variable lista
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    posts_serialized2 = serializers.serialize('json', lista2) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized,"listado2":posts_serialized2}) # regresa la informacion en formato json

# LISTADO DE SISTEMAS Y SUBSISTEMAS

# def listarSistemas(request):
#     queryset =request.GET.get("buscar")
#     sistema=Sistema.objects.all().order_by('nombre')
#     subsistema=SubSistema.objects.all().order_by('nombre')
#     if queryset:
#         sistema=Sistema.objects.filter(
#             Q(nombre__icontains = queryset) |
#             Q(codigo__icontains = queryset)).distinct()         #LISTAR Y FILTRAR SISTEMAS Y SUB-SISTEMAS
#         subsistema=SubSistema.objects.filter(
#             Q(nombre__icontains = queryset) |
#             Q(codigo__icontains = queryset)).distinct()
    
#     contexto ={'sistemas':sistema,'subsistemas':subsistema}
#     return render(request,'listado_sistemas.html',contexto) 


class listarSistemas(ListView):
    model= Sistema
    template_name='listado_sistemas.html'
    context_object_name='sistemas'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Sistema.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class listarSubsistemas(ListView):
    model= SubSistema
    template_name='listado_sistemas.html'
    context_object_name='subsistemas'
    paginate_by=20
    ordering = ['codigo']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return SubSistema.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class lista_s_editar(UpdateView):
    model=Sistema
    form_class=FormularioSistema                #EDITAR SISTEMAS
    template_name="registro_sistema.html"
    success_url=reverse_lazy("listado_sistemas")

class lista_ss_editar(UpdateView):
    model=SubSistema
    form_class=FormularioSubSistema                #EDITAR SUBSISTEMAS
    template_name="registro_subsistema.html"
    success_url=reverse_lazy("listado_subsistemas")

class lista_s_eliminar(DeleteView):
    model=Sistema                                   #ELIMINAR SISTEMAS
    template_name="listado_sistemas_eliminar.html"
    success_url=reverse_lazy("listado_sistemas")

class lista_ss_eliminar(DeleteView):
    model=SubSistema                                   #ELIMINAR SUBSISTEMAS
    template_name="listado_sistemas_eliminar.html"
    success_url=reverse_lazy("listado_subsistemas")

def vista_listado_sistemas(request):
    lista=Sistema.objects.all()  # asignar valores desde los modelos a la variable lista
    lista2=SubSistema.objects.all()  # asignar valores desde los modelos a la variable lista
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    posts_serialized2 = serializers.serialize('json', lista2) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized,"listado2":posts_serialized2}) # regresa la informacion en formato json

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#REPORTES PDF///////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#EQUIPOS PRINCIPALES///////////////

class generar_reporte_equipoPr(ListView):
    model= EquipoPrincipal
    template_name='reporte_equipoPr.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(id=conf_id)
        return qs
#REPORTE TOTAL PRINCIPALES///////////

class generar_reporte_equipoPr_total(ListView):
    model= EquipoPrincipal
    template_name='reporte_equipoPr_total.html'
    context_object_name='confspr'
    ordering = ['codigo']

#EQUIPOS SECUNDARIOS////////////////

class generar_reporte_equipoSec(ListView):
    model= Equipo
    template_name='reporte_equipoSec.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=Equipo.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(id=conf_id)
        return qs

#REPORTE TOTAL SECUNDARIO///////////

class generar_reporte_equipoSec_total(ListView):
    model= Equipo
    template_name='reporte_equipoSec_total.html'
    context_object_name='confspr'
    ordering = ['codigo']

#SUBSISTEMAS ////////////////

class generar_reporte_subsistemas(ListView):
    model= EquipoPrincipal
    template_name='reporte_subsistemas.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(subsistema_id=conf_id)
        return qs 
    
    
def reporte_listado_subsistemas(self):
    lista=Equipo.objects.all()  

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

#SISTEMAS ////////////////

class generar_reporte_sistemas(ListView):
    model= EquipoPrincipal
    template_name='reporte_sistemas.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(sistema_id=conf_id)
        return qs 
    
    
def reporte_listado_sistemas(self):
    lista=Equipo.objects.all()  

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

#PLANTAS SECUNDARIAS ////////////////

class generar_reporte_plantas_secundarias(ListView):
    model= EquipoPrincipal
    template_name='reporte_plantas_secundarias.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(planta_secundaria_id=conf_id)
        return qs 
    
    
def reporte_listado_plantas_secundarias(self):
    lista=Equipo.objects.all()  

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

#PLANTAS PRINCIPALES ////////////////

class generar_reporte_plantas(ListView):
    model= EquipoPrincipal
    template_name='reporte_plantas.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(planta_id=conf_id)
        return qs 
    
    
def reporte_listado_plantas(self):
    lista=Equipo.objects.all()  

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

#TIPOS DE EQUIPO ////////////////

class listarTiposEquipos2(ListView):
    model= TipoDeEquipo
    template_name='listado_tipos_equipo.html'
    context_object_name='tipos'
    paginate_by=20
    ordering = ['nombre']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return TipoDeEquipo.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])).distinct()

        return super().get_queryset()

class generar_reporte_tiposEquipoPr(ListView):
    model= EquipoPrincipal
    template_name='reporte_tipos_equipo.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=EquipoPrincipal.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(tipo_id=conf_id)
        return qs 
    
    
def reporte_listado_tiposEquipoSec(self):
    lista=Equipo.objects.all()  

    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json