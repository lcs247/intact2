from tkinter import E
from typing import OrderedDict
from django.contrib.messages.api import success,error
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import *
from .forms import FormularioCategoria, FormularioCosto, FormularioCriticidad,FormularioCriticidadCPr,FormularioCriticidadCSec, FormularioCriticidadPr, FormularioExposicion, FormularioMdA, FormularioOcurrencia, FormularioPerdida, FormularioRedundancia, FormularioSegysa
from django.http import JsonResponse
from django.core import serializers
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from sicor.utils import render_to_pdf

# Create your views here.

#LISTAR CRITICIDADES SIMPLES

# def listarCriticidad(request):
#     queryset =request.GET.get("buscar")
#     criticidad_pr=CriticidadPr.objects.all().order_by('activo')
#     # criticidad=Criticidad.objects.all().order_by('activo')
    
#     if queryset:
#         criticidad_pr=CriticidadPr.objects.filter(
#             Q(nombre__icontains = queryset)).distinct()         #LISTAR Y FILTRAR EQUIPOS SECUNDARIOS Y PRINCIPALES

#         # criticidad=Criticidad.objects.filter(
#             # Q(nombre__icontains = queryset)).distinct()

#     contexto ={'criticidades_pr':criticidad_pr}
#     return render(request,'criticidad_muestra.html',contexto)

class listarCriticidad(ListView):
    model= Criticidad
    template_name='criticidad_muestra.html'
    context_object_name='criticidades'
    paginate_by=20
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Criticidad.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])
            ).distinct()

        return super().get_queryset()

class listarCriticidadPr(ListView):
    model= CriticidadPr
    template_name='criticidad_muestra.html'
    context_object_name='criticidadesPr'
    paginate_by=20
    
    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return CriticidadPr.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])
            ).distinct()
        
        return super().get_queryset()

#CRITICIDAD SIMPLE PRINCIPAL

class formularioCriticidadPr(CreateView):
    model=CriticidadPr
    form_class=FormularioCriticidadPr
    template_name="criticidad_form2.html"
    success_url=reverse_lazy("criticidad_muestra_Pr")

class listacrit_editar_Pr(UpdateView):
    model=CriticidadPr
    form_class=FormularioCriticidadPr
    template_name="criticidad_form2.html"
    success_url=reverse_lazy("criticidad_muestra_Pr")

class listacrit_eliminar_Pr(DeleteView):
    model=CriticidadPr
    template_name="criticidad_eliminar.html"
    success_url=reverse_lazy("criticidad_muestra_Pr")

#CRITICIDAD SIMPLE SECUNDARIA

class formularioCriticidad(CreateView):
    model=Criticidad
    form_class=FormularioCriticidad
    template_name="criticidad_form.html"
    success_url=reverse_lazy("criticidad_muestra")
 

class listacrit_editar(UpdateView):
    model=Criticidad
    form_class=FormularioCriticidad
    template_name="criticidad_form.html"
    success_url=reverse_lazy("criticidad_muestra")

class listacrit_eliminar(DeleteView):
    model=Criticidad
    template_name="criticidad_eliminar.html"
    success_url=reverse_lazy("criticidad_muestra")

#LISTAR CRITICIDADES COMPLETAS

class listarCriticidadCSec(ListView):
    model= CriticidadCSec
    template_name='criticidad_muestra2.html'
    context_object_name='criticidades'
    paginate_by=20
    ordering = ['tag']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return CriticidadCSec.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar']) |
                Q(ctdr__icontains = self.request.GET['buscar'])
            ).distinct()

        return super().get_queryset()

class listarCriticidadCPr(ListView):
    model= CriticidadCPr
    template_name='criticidad_muestra2.html'
    context_object_name='criticidadesPr'
    paginate_by=20
    ordering = ['tag']

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return CriticidadCPr.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar']) |
                Q(ctdr__icontains = self.request.GET['buscar'])
            ).distinct()
        
        return super().get_queryset()

#CRITICIDAD COMPLETA PRINCIPAL

class formularioCriticidadCPr(CreateView):
    model=CriticidadCPr
    form_class=FormularioCriticidadCPr
    template_name="criticidad_form3.html"
    success_url=reverse_lazy("criticidad_muestra_CPr")

class listacrit_editar_CPr(UpdateView):
    model=CriticidadCPr
    form_class=FormularioCriticidadCPr
    template_name="criticidad_form3.html"
    success_url=reverse_lazy("criticidad_muestra_CPr")

class listacrit_eliminar_CPr(DeleteView):
    model=CriticidadCPr
    template_name="criticidad_eliminar.html"
    success_url=reverse_lazy("criticidad_muestra_CPr")

# class generar_reporte_criticidadCPr(ListView):   
#     def get(self,request,*args,**kwargs):
#         template_name='reporte_criticidad.html'
#         criticidad=CriticidadCPr.objects.all()
#         conf_id=self.request.GET.get('lang')
#         if conf_id:
#             criticidad=criticidad.filter(activo__id=conf_id)
#         data={
#             'criticidades':criticidad,
#         }
#         pdf=render_to_pdf(template_name,data)
#         return HttpResponse(pdf,content_type='application/pdf')

#CRITICIDAD COMPLETA SECUNDARIA

class formularioCriticidadCSec(CreateView):
    model=CriticidadCSec
    form_class=FormularioCriticidadCSec
    template_name="criticidad_form4.html"
    success_url=reverse_lazy("criticidad_muestra_CSec")
 

class listacrit_editar_CSec(UpdateView):
    model=CriticidadCSec
    form_class=FormularioCriticidadCSec
    template_name="criticidad_form4.html"
    success_url=reverse_lazy("criticidad_muestra_CSec")

class listacrit_eliminar_Csec(DeleteView):
    model=CriticidadCSec
    template_name="criticidad_eliminar.html"
    success_url=reverse_lazy("criticidad_muestra_CSec")

# class generar_reporte_criticidadCSec(ListView):   
#     def get(self,request,*args,**kwargs):
#         template_name='reporte_criticidad.html'
#         criticidad=CriticidadCSec.objects.all()
#         conf_id=self.request.GET.get('lang')
#         if conf_id:
#             criticidad=criticidad.filter(activo__id=conf_id)
#         data={
#             'criticidades':criticidad,
#         }
#         pdf=render_to_pdf(template_name,data)
#         return HttpResponse(pdf,content_type='application/pdf')

#/////////////////////////////////////////////////////////////////////////////////////////////////////
#REPORTES PDF///////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////

#EQUIPOS PRINCIPALES///////////////

class generar_reporte_CriticidadCequipoPr(ListView):
    model= CriticidadCPr
    template_name='reporte_criticidad.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=CriticidadCPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo_id=conf_id)
        return qs

#EQUIPOS SECUNDARIOS///////////////

class generar_reporte_CriticidadCequipoSec(ListView):
    model= CriticidadCSec
    template_name='reporte_criticidad.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=CriticidadCSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo_id=conf_id)
        return qs
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#LISTAR CONFIGURACIONES

def listarParametros(request):
    redundancia=Redundancia.objects.all().order_by('valor')
    ocurrencia=Ocurrencia.objects.all().order_by('valor')
    segysa=Segysa.objects.all().order_by('valor')
    mda=MdA.objects.all().order_by('valor')
    costo=Costo.objects.all().order_by('valor')
    perdida=Perdida.objects.all().order_by('valor')
    exposicion=Exposicion.objects.all().order_by('valor')
    categoria=CategoriaRiesgo.objects.all().order_by('descripcion')

    contexto ={'redundancias':redundancia,'ocurrencias':ocurrencia,
    'segysas':segysa,'mdas':mda,'costos':costo,
    'perdidas':perdida,'exposiciones':exposicion,'categorias':categoria}
    return render(request,'criticidad_configuracion.html',contexto)

def vista_listado_cat(request):
    lista=CategoriaRiesgo.objects.all()  # asignar valores desde los modelos a la variable lista
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

# class listarRedundancia(ListView):
#     model= Redundancia
#     template_name='criticidad_configuracion.html'
#     context_object_name='redundancias'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Redundancia.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarOcurrencia(ListView):
#     model= Ocurrencia
#     template_name='criticidad_configuracion.html'
#     context_object_name='ocurrencias'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Ocurrencia.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarSegysa(ListView):
#     model= Segysa
#     template_name='criticidad_configuracion.html'
#     context_object_name='segysas'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Segysa.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarMdA(ListView):
#     model= MdA
#     template_name='criticidad_configuracion.html'
#     context_object_name='mdas'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return MdA.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarCosto(ListView):
#     model= Costo
#     template_name='criticidad_configuracion.html'
#     context_object_name='costos'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Costo.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarPerdida(ListView):
#     model= Perdida
#     template_name='criticidad_configuracion.html'
#     context_object_name='perdidas'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Perdida.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

# class listarExposicion(ListView):
#     model= Exposicion
#     template_name='criticidad_configuracion.html'
#     context_object_name='segysas'
#     paginate_by=10

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return Exposicion.objects.filter(
#                 Q(descripcion__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()

#CONFIGURACIONES DE CRITICIDAD
#CATEGORIAS
class formularioCategoria(CreateView):
    model=CategoriaRiesgo
    form_class=FormularioCategoria
    template_name="criticidad_form6.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Categoria(UpdateView):
    model=CategoriaRiesgo
    form_class=FormularioCategoria
    template_name="criticidad_form6.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Categoria(DeleteView):
    model=CategoriaRiesgo
    template_name="criticidad_eliminar_categoria.html"
    success_url=reverse_lazy("criticidad_conf")

#REDUNDANCIA
class formularioRedundancia(CreateView):
    model=Redundancia
    form_class=FormularioRedundancia
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Redundancia(UpdateView):
    model=Redundancia
    form_class=FormularioRedundancia
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Redundancia(DeleteView):
    model=Redundancia
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")

#OCURRENCIA
class formularioOcurrencia(CreateView): 
    model=Ocurrencia
    form_class=FormularioOcurrencia
    template_name="criticidad_form7.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Ocurrencia(UpdateView):
    model=Ocurrencia
    form_class=FormularioOcurrencia
    template_name="criticidad_form7.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Ocurrencia(DeleteView):
    model=Ocurrencia
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf") 

def vista_listado_ocurrenciasSec(request):
    lista=Ocurrencia.objects.all()  # asignar valores desde los modelos a la variable lista
    posts_serialized = serializers.serialize('json', lista) # se da formato json a la lista de archivos
    return JsonResponse({"listado":posts_serialized}) # regresa la informacion en formato json

#SEGYSA
class formularioSegysa(CreateView):
    model=Segysa
    form_class=FormularioSegysa
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Segysa(UpdateView):
    model=Segysa
    form_class=FormularioSegysa
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Segysa(DeleteView):
    model=Segysa
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")

#MDA
class formularioMDA(CreateView):
    model=MdA
    form_class=FormularioMdA
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_MDA(UpdateView):
    model=MdA
    form_class=FormularioMdA
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_MDA(DeleteView):
    model=MdA
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")

#COSTO
class formularioCosto(CreateView):
    model=Costo
    form_class=FormularioCosto
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Costo(UpdateView):
    model=Costo
    form_class=FormularioCosto
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Costo(DeleteView):
    model=Costo
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")

#PERDIDA
class formularioPerdida(CreateView):
    model=Perdida
    form_class=FormularioPerdida
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Perdida(UpdateView):
    model=Perdida
    form_class=FormularioPerdida
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Perdida(DeleteView):
    model=Perdida
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")

#EXPOSICIÓN
class formularioExposicion(CreateView):
    model=Exposicion
    form_class=FormularioExposicion
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")
 
class listacrit_editar_Exposicion(UpdateView):
    model=Exposicion
    form_class=FormularioExposicion
    template_name="criticidad_form5.html"
    success_url=reverse_lazy("criticidad_conf")

class listacrit_eliminar_Exposicion(DeleteView):
    model=Exposicion
    template_name="criticidad_eliminar_configuracion.html"
    success_url=reverse_lazy("criticidad_conf")