from typing import List
from django.shortcuts import render,redirect

from sicor.utils import render_to_pdf
from .models import *
from django.db.models import Q
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView,View
from django.http import JsonResponse,HttpResponse
from django.core import serializers
from django.urls import reverse_lazy
from .forms import FormResultConfPr, FormResultConfPrFltr, FormResultConfSec, FormResultConfSecFltr, FormResultConfSubsistema, FormularioConfiabilidadPr, FormularioConfiabilidadSec
from registro.models import *
from django.template import RequestContext


# Create your views here.

# class listarCriticidadCSec(ListView):
#     model= CriticidadCSec
#     template_name='criticidad_muestra2.html'
#     context_object_name='criticidades'
#     paginate_by=20
#     ordering = ['tag']

#     def get_queryset(self):
#         if self.request.GET.get('buscar') is not None:
#             return CriticidadCSec.objects.filter(
#                 Q(nombre__icontains = self.request.GET['buscar']) |
#                 Q(ctdr__icontains = self.request.GET['buscar'])
#             ).distinct()

#         return super().get_queryset()
#///////////////////////////////////////////////////////////////////////////////////////////////////////
#EQUIPOS PRINCIPALES
#/////////////////////////////////////////////////////////////////////////////////////////////////////
def buscarConfiabilidadPr(request):                         #PASAR JSON A PLANTILLAS
    lista=ConfiabilidadEquipoPr.objects.all()
    posts_serialized = serializers.serialize('json', lista)
    contexto ={'listado':posts_serialized}
    return JsonResponse(contexto)

class formularioConfiabilidadPr(CreateView):
    model=ConfiabilidadEquipoPr
    form_class=FormularioConfiabilidadPr                    #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_form.html"
    success_url=reverse_lazy("confiabilidad_muestra")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class listarConfiabilidadEquiposPr(ListView):   #EQUIPOS --->IDIOMAS
    model= EquipoPrincipal
    template_name='confiabilidad_muestra.html'
    context_object_name='equipospr'
    ordering = ['codigo']
    paginate_by=20

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return EquipoPrincipal.objects.filter(
                Q(codes__icontains = self.request.GET['buscar'])|
                Q(nombre__icontains = self.request.GET['buscar'])
                
            ).distinct()
        
        return super().get_queryset()

class listarConfiabilidades(ListView):  #CONFIABILIDADES ---->FRASES
    model= ConfiabilidadEquipoPr
    template_name='confiabilidad_detalle.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs
    # def vista_formulario(request):
    #     if request.method == 'GET':
    #         form = FormResultConfPr(request.GET, request.FILES)
    #         if form.is_valid():
    #             form.save()
    #         return redirect('confiabilidad_detalle.html')      
    #     else:
    #         form = FormResultConfPr()
    #     return render (request,"confiabilidad_detalle.html",{'form':form})

class listaconfiabilidad_editar_Pr(UpdateView):
    model=ConfiabilidadEquipoPr
    form_class=FormularioConfiabilidadPr
    template_name="confiabilidad_form.html"
    success_url=reverse_lazy("confiabilidad_muestra")

class listaconfiabilidad_eliminar_Pr(DeleteView):
    model=ConfiabilidadEquipoPr
    template_name="confiabilidad_eliminar.html"
    success_url=reverse_lazy("confiabilidad_muestra")

class formResultConfPr(CreateView):
    model=ResultadosConfActivo
    form_class=FormResultConfPr                    #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_resultadosform.html"
    success_url=reverse_lazy("confiabilidad_muestra")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class formResultConfPrfiltr(CreateView):
    model=ResultadosConfActivoFltr
    form_class=FormResultConfPrFltr                 #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_resultadosformfiltrado.html"
    success_url=reverse_lazy("confiabilidad_muestra")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs
        
class filtrarConfiabilidades(ListView):  #CONFIABILIDADES ---->FRASES
    model= ConfiabilidadEquipoPr
    template_name='confiabilidad_filtrarfechas.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs
#///////////////////////////////////////////////////////////////////////////////////////////////////////
#EQUIPOS SECUNDARIOS
#///////////////////////////////////////////////////////////////////////////////////////////////////////
def buscarConfiabilidadSec(request):
    queryset =request.GET.get("buscar")
    lista=ConfiabilidadEquipoSec.objects.all()
    posts_serialized = serializers.serialize('json', lista)

    contexto ={'listado':posts_serialized}
    return JsonResponse(contexto)

class formularioConfiabilidadSec(CreateView):
    model=ConfiabilidadEquipoSec
    form_class=FormularioConfiabilidadSec                    #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_form2.html"
    success_url=reverse_lazy("confiabilidad_muestra2")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class listarConfiabilidadEquiposSec(ListView):   #EQUIPOS --->IDIOMAS
    model= Equipo
    template_name='confiabilidad_muestra2.html'
    context_object_name='equipospr'
    ordering = ['codigo']
    paginate_by=20

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return Equipo.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])
            ).distinct()
        
        return super().get_queryset()

class listarConfiabilidadesSec(ListView):  #CONFIABILIDADES ---->FRASES
    model= ConfiabilidadEquipoSec
    template_name='confiabilidad_detalle2.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class listaconfiabilidad_editar_Sec(UpdateView):
    model=ConfiabilidadEquipoSec
    form_class=FormularioConfiabilidadSec
    template_name="confiabilidad_form2.html"
    success_url=reverse_lazy("confiabilidad_muestra2")

class listaconfiabilidad_eliminar_Sec(DeleteView):
    model=ConfiabilidadEquipoSec
    template_name="confiabilidad_eliminar.html"
    success_url=reverse_lazy("confiabilidad_muestra2")

class formResultConfSec(CreateView):
    model=ResultadosConfActivoSec
    form_class=FormResultConfSec                   #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_resultadosform2.html"
    success_url=reverse_lazy("confiabilidad_muestra2")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class formResultConfSecfiltr(CreateView):
    model=ResultadosConfActivoSecFltr
    form_class=FormResultConfSecFltr                    #FORMULARIO DE REGISTRO DE FALLA
    template_name="confiabilidad_resultadosform2filtrado.html"
    success_url=reverse_lazy("confiabilidad_muestra2")
    
    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class filtrarConfiabilidadesSec(ListView):  #CONFIABILIDADES ---->FRASES
    model= ConfiabilidadEquipoSec
    template_name='confiabilidad_filtrarfechasSec.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs
#////////////////////////////////////////////////////////////////////////////////////////////////////////////
#REPORTE PDF/////////////////////////////////////////////////////////////////////////////////////////////////////
#EQUIPOS PRINCIPALES ///////////////////////////////////////////////////////////////////////////////////////////

# class generar_reporte_confiabilidadPr(ListView):
    
#     def get(self,request,*args,**kwargs):
#         template_name='reporte_confiabilidad_detalle.html'
#         confiabilidad=ConfiabilidadEquipoPr.objects.all()
#         resultado=ResultadosConfActivo.objects.all()
#         conf_id=self.request.GET.get('lang')
#         if conf_id:
#             confiabilidad=confiabilidad.filter(activo__id=conf_id)
#             resultado=resultado.filter(activo__id=conf_id)

#         data={
#             'confiabilidades':confiabilidad,
#             'resultados':resultado
#         }
#         pdf=render_to_pdf(template_name,data)
#         return HttpResponse(pdf,content_type='application/pdf')

class generar_reporte_confiabilidadPrueba(ListView):
    model= ConfiabilidadEquipoPr
    template_name='confiabilidad_reporte_pdf_Pr.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class generar_reporte_confiabilidadPruebaFltr(ListView):
    model= ConfiabilidadEquipoPr
    template_name='confiabilidad_reporte_pdf_PrFltr.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang').split('?lang')
        print(conf_id)
        if conf_id:
            qs=qs.filter(activo__id=conf_id[0])
        return qs

#EQUIPOS SECUNDARIOS ///////////////////////////////////////////////////////////////////////////////////////////
# class generar_reporte_confiabilidadSec(ListView):
    
#     def get(self,request,*args,**kwargs):
#         template_name='reporte_confiabilidad_detalle.html'
#         confiabilidad=ConfiabilidadEquipoSec.objects.all()
#         resultado=ResultadosConfActivoSec.objects.all()
#         conf_id=self.request.GET.get('lang')
#         if conf_id:
#             confiabilidad=confiabilidad.filter(activo__id=conf_id)
#             resultado=resultado.filter(activo__id=conf_id)

#         data={
#             'confiabilidades':confiabilidad,
#             'resultados':resultado
#         }
#         pdf=render_to_pdf(template_name,data)
#         return HttpResponse(pdf,content_type='application/pdf')

class generar_reporte_confiabilidadPruebaSec(ListView):
    model= ConfiabilidadEquipoSec
    template_name='confiabilidad_reporte_pdf_Sec.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(activo__id=conf_id)
        return qs

class generar_reporte_confiabilidadPruebaSecFltr(ListView):
    model= ConfiabilidadEquipoSec
    template_name='confiabilidad_reporte_pdf_SecFltr.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoSec.objects.all()
        conf_id=self.request.GET.get('lang').split('?lang')
        print(conf_id)
        if conf_id:
            qs=qs.filter(activo__id=conf_id[0])
        return qs
   
#///////////////////////////////////////////////////////////////////////////////////////////////////////
#SUBSISTEMAS
#///////////////////////////////////////////////////////////////////////////////////////////////////////

class listarConfSubsitemas(ListView):   #SUBSISTEMAS --->IDIOMAS
    model= SubSistema
    template_name='confiabilidad_muestra_subsistema.html'
    context_object_name='equipospr'
    ordering = ['codigo']
    paginate_by=20

    def get_queryset(self):
        if self.request.GET.get('buscar') is not None:
            return SubSistema.objects.filter(
                Q(nombre__icontains = self.request.GET['buscar'])|
                Q(codigo__icontains = self.request.GET['buscar'])

            ).distinct()
        
        return super().get_queryset()

class listarConfiabilidades_subsistema(ListView):  #CONFIABILIDADES ---->FRASES
    model= ConfiabilidadEquipoPr
    template_name='confiabilidad_detalle_subsistema.html'
    context_object_name='confspr'

    def get_queryset(self):
        qs=ConfiabilidadEquipoPr.objects.all()
        conf_id=self.request.GET.get('lang')
        if conf_id:
            qs=qs.filter(subsistema=conf_id)
        return qs

 