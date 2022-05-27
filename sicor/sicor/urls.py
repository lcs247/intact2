"""sicor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from registro.views import *
from criticidad.views import *
from confiabilidad.views import *
from fallas_funcionales.views import *
from reportConfig.views import *
from django.contrib.auth.views import LoginView,logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', login_required(listarConfig.as_view()), name='inicio'),
    path('registro-equipos', login_required(formularioEquipo.as_view()), name='registro_equipos'),
    path('registro-equipos-pr', login_required(formularioEquipoPrincipal.as_view()), name='registro_equipos_principal'),
    path('registro-sistema', login_required(formularioSistema.as_view()), name='registro_sistema'),
    path('registro-subsistema', login_required(formularioSubSistema.as_view()), name='registro_subsistema'),
    path('registro-planta', login_required(formularioPlanta.as_view()), name='registro_planta'),
    path('registro-planta-sec', login_required(formularioPlantaSecundaria.as_view()), name='registro_planta_secundaria'),
    path('activos', login_required(listarEquipos.as_view()), name='registro_muestra'),
    path('activos_Pr', login_required(listarEquiposPr.as_view()), name='registro_muestra_Pr'),
    path('activos/tiposEquipos', login_required(listarTiposEquipos2.as_view()), name='listado_tiposEquipos'),
    path('criticidad-form', login_required(formularioCriticidad.as_view()), name='criticidad_form'),
    path('criticidad-form-Pr', login_required(formularioCriticidadPr.as_view()), name='criticidad_form_Pr'),
    path('criticidad-form-CSec', login_required(formularioCriticidadCSec.as_view()), name='criticidad_form_CSec'),
    path('criticidad-form-CPr', login_required(formularioCriticidadCPr.as_view()), name='criticidad_form_CPr'),
    path('activos/editar/(?p<pk>\d+)/', login_required(lista_editar.as_view()), name='lista_editar'),
    path('activos/eliminar/(?p<pk>\d+)/', login_required(lista_eliminar.as_view()), name='lista_eliminars'),
    path('activos/editar_pr/(?p<pk>\d+)/', login_required(lista_editar_pr.as_view()), name='lista_editar_pr'),
    path('activos/eliminar_pr/(?p<pk>\d+)/', login_required(lista_eliminar_pr.as_view()), name='lista_eliminar'),
    #path('criticidad', login_required(listarCriticidad.as_view()), name='criticidad_muestra'),
    path('listado_cat/', vista_listado_cat, name='vista_listado_cat'),
    path('listado_conf/', buscarConfiabilidadPr, name='buscar_listado_conf'),
    path('listado_ocu/', vista_listado_ocurrenciasSec, name='vista_listado_ocurrenciasSec'),
    path('confiabilidad-form', login_required(formularioConfiabilidadPr.as_view()), name='confiabilidad_form'),
    path('confiabilidad-muestra', login_required(listarConfiabilidadEquiposPr.as_view()), name='confiabilidad_muestra'),
    path('confiabilidad-detalle',login_required(listarConfiabilidades.as_view()), name='detalle_confiabilidad'),
    path('confiabilidad/editar/<int:pk>/',login_required(listaconfiabilidad_editar_Pr.as_view()), name='listaPr_confiabilidad_editar'),
    path('confiabilidad/eliminar/<int:pk>/',login_required(listaconfiabilidad_eliminar_Pr.as_view()), name='listaPr_confiabilidad_eliminar'),
    path('listado_conf_Sec/', buscarConfiabilidadSec, name='buscar_listado_confSec'),
    path('confiabilidad-formSec', login_required(formularioConfiabilidadSec.as_view()), name='confiabilidad_form2'),
    path('confiabilidad-muestraSec', login_required(listarConfiabilidadEquiposSec.as_view()), name='confiabilidad_muestra2'),
    path('confiabilidad-detalleSec',login_required(listarConfiabilidadesSec.as_view()), name='detalle_confiabilidad2'),
    path('confiabilidad/editarSec/<int:pk>/',login_required(listaconfiabilidad_editar_Sec.as_view()), name='listaSec_confiabilidad_editar'),
    path('confiabilidad/eliminarSec/<int:pk>/',login_required(listaconfiabilidad_eliminar_Sec.as_view()), name='listaSec_confiabilidad_eliminar'),
    #path('criticidad_Pr', login_required(listarCriticidadPr.as_view()), name='criticidad_muestra_Pr'),
    path('criticidad_CPr', login_required(listarCriticidadCPr.as_view()), name='criticidad_muestra_CPr'),
    path('criticidad_CSec', login_required(listarCriticidadCSec.as_view()), name='criticidad_muestra_CSec'),
    #path('criticidad/editar/(?p<pk>\d+)/', login_required(listacrit_editar.as_view()), name='listacrit_editar'),
    #path('criticidad/eliminar/(?p<pk>\d+)/', login_required(listacrit_eliminar.as_view()), name='listacrit_eliminar'),
    #path('criticidad/editar_pr/(?p<pk>\d+)/', login_required(listacrit_editar_Pr.as_view()), name='listacrit_editar_Pr'),
    #path('criticidad/eliminar_pr/(?p<pk>\d+)/', login_required(listacrit_eliminar_Pr.as_view()), name='listacrit_eliminar_Pr'),
    path('criticidad/editar_cpr/(?p<pk>\d+)/', login_required(listacrit_editar_CPr.as_view()), name='listacrit_editar_CPr'),
    path('criticidad/eliminar_cpr/(?p<pk>\d+)/', login_required(listacrit_eliminar_CPr.as_view()), name='listacrit_eliminar_CPr'),
    path('criticidad/editar_csec/(?p<pk>\d+)/', login_required(listacrit_editar_CSec.as_view()), name='listacrit_editar_CSec'),
    path('criticidad/eliminar_csec/(?p<pk>\d+)/', login_required(listacrit_eliminar_Csec.as_view()), name='listacrit_eliminar_CSec'),
    path('', LoginView.as_view(template_name='login.html'),name='login1'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'),name='login'),
    path('logout/', logout_then_login,name='logout'),
    path('listado_activos/', vista_listado_activos, name='vista_listado_activos'),
    path('planta', login_required(listarPlantas.as_view()), name='listado_plantas'),
    path('planta_Sec', login_required(listarPlantasSec.as_view()), name='listado_plantas_Sec'),
    path('planta/editar/(?p<pk>\d+)/', login_required(lista_p_editar.as_view()), name='lista_p_editar'),
    path('planta/eliminar/(?p<pk>\d+)/', login_required(lista_p_eliminar.as_view()), name='lista_p_eliminar'),
    path('planta/editar_sec/(?p<pk>\d+)/', login_required(lista_psec_editar.as_view()), name='lista_psec_editar'),
    path('planta/eliminar_sec/(?p<pk>\d+)/', login_required(lista_psec_eliminar.as_view()), name='lista_psec_eliminar'),
    path('listado_plantas/', vista_listado_plantas, name='vista_listado_plantas'),
    path('sistemas', login_required(listarSistemas.as_view()), name='listado_sistemas'),
    path('subsistemas', login_required(listarSubsistemas.as_view()), name='listado_subsistemas'),
    path('sistemas/editar/(?p<pk>\d+)/', login_required(lista_s_editar.as_view()), name='lista_s_editar'),
    path('sistemas/eliminar/(?p<pk>\d+)/', login_required(lista_s_eliminar.as_view()), name='lista_s_eliminar'),
    path('sistemas/editar_ss/(?p<pk>\d+)/', login_required(lista_ss_editar.as_view()), name='lista_ss_editar'),
    path('sistemas/eliminar_ss/(?p<pk>\d+)/', login_required(lista_ss_eliminar.as_view()), name='lista_ss_eliminar'),    
    path('listado_sistemas/', vista_listado_sistemas, name='vista_listado_sistemas'),
    path('criticidad/conf/', login_required(listarParametros), name='criticidad_conf'), 
    path('criticidad/conf/form_Red', login_required(formularioRedundancia.as_view()), name='registro_Redundancia'),    
    path('criticidad/conf/editar_Red/(?p<pk>\d+)/', login_required(listacrit_editar_Redundancia.as_view()), name='listacrit_editar_Redundancia'),
    path('criticidad/conf/eliminar_Red/(?p<pk>\d+)/', login_required(listacrit_eliminar_Redundancia.as_view()), name='listacrit_eliminar_Redundancia'),    
    path('criticidad/conf/form_Ocu', login_required(formularioOcurrencia.as_view()), name='registro_Ocurrencia'),    
    path('criticidad/conf/editar_Ocu/(?p<pk>\d+)/', login_required(listacrit_editar_Ocurrencia.as_view()), name='listacrit_editar_Ocurrencia'),
    path('criticidad/conf/eliminar_Ocu/(?p<pk>\d+)/', login_required(listacrit_eliminar_Ocurrencia.as_view()), name='listacrit_eliminar_Ocurrencia'),
    path('criticidad/conf/form_Segysa', login_required(formularioSegysa.as_view()), name='registro_Segysa'),    
    path('criticidad/conf/editar_Segysa/(?p<pk>\d+)/', login_required(listacrit_editar_Segysa.as_view()), name='listacrit_editar_Segysa'),
    path('criticidad/conf/eliminar_Segysa/(?p<pk>\d+)/', login_required(listacrit_eliminar_Segysa.as_view()), name='listacrit_eliminar_Segysa'),
    path('criticidad/conf/form_MDA', login_required(formularioMDA.as_view()), name='registro_MDA'),    
    path('criticidad/conf/editar_MDA/(?p<pk>\d+)/', login_required(listacrit_editar_MDA.as_view()), name='listacrit_editar_MDA'),
    path('criticidad/conf/eliminar_MDA/(?p<pk>\d+)/', login_required(listacrit_eliminar_MDA.as_view()), name='listacrit_eliminar_MDA'),
    path('criticidad/conf/form_costo', login_required(formularioCosto.as_view()), name='registro_Costo'),    
    path('criticidad/conf/editar_costo/(?p<pk>\d+)/', login_required(listacrit_editar_Costo.as_view()), name='listacrit_editar_Costo'),
    path('criticidad/conf/eliminar_costo/(?p<pk>\d+)/', login_required(listacrit_eliminar_Costo.as_view()), name='listacrit_eliminar_Costo'),
    path('criticidad/conf/form_perdida', login_required(formularioPerdida.as_view()), name='registro_Perdida'),    
    path('criticidad/conf/editar_perdida/(?p<pk>\d+)/', login_required(listacrit_editar_Perdida.as_view()), name='listacrit_editar_Perdida'),
    path('criticidad/conf/eliminar_perdida/(?p<pk>\d+)/', login_required(listacrit_eliminar_Perdida.as_view()), name='listacrit_eliminar_Perdida'),
    path('criticidad/conf/form_exp', login_required(formularioExposicion.as_view()), name='registro_Exposicion'),    
    path('criticidad/conf/editar_exp/(?p<pk>\d+)/', login_required(listacrit_editar_Exposicion.as_view()), name='listacrit_editar_Exposicion'),
    path('criticidad/conf/eliminar_exp/(?p<pk>\d+)/', login_required(listacrit_eliminar_Exposicion.as_view()), name='listacrit_eliminar_Exposicion'),
    path('criticidad/conf/form_cat', login_required(formularioCategoria.as_view()), name='registro_Categoria'),    
    path('criticidad/conf/editar_cat/(?p<pk>\d+)/', login_required(listacrit_editar_Categoria.as_view()), name='listacrit_editar_Categoria'),
    path('criticidad/conf/eliminar_cat/(?p<pk>\d+)/', login_required(listacrit_eliminar_Categoria.as_view()), name='listacrit_eliminar_Categoria'),
    path('criticidad/report-activoCPr/', login_required(generar_reporte_CriticidadCequipoPr.as_view()), name='reporte_criticidad_CPr'),    
    path('criticidad/report-activoCSec/', login_required(generar_reporte_CriticidadCequipoSec.as_view()), name='reporte_criticidad_CSec'),    
    #path('confiabilidad/report-activoPr/', login_required(generar_reporte_confiabilidadPr.as_view()), name='reporte_confiabilidad'),    
    #path('confiabilidad/report-activoSec/', login_required(generar_reporte_confiabilidadSec.as_view()), name='reporte_confiabilidad_Sec'),    
    path('confiabilidad-detalle/result/', login_required(formResultConfPr.as_view()), name='form_resultPr'),    
    path('confiabilidad-detalle/filtrar/', login_required(filtrarConfiabilidades.as_view()), name='filtrar_confiabilidad'),    
    path('confiabilidad-detalle/resultfiltr/', login_required(formResultConfPrfiltr.as_view()), name='form_resultPr_filtr'),    
    path('confiabilidad-detalleSec/result/', login_required(formResultConfSec.as_view()), name='form_resultSec'),    
    path('confiabilidad-detalleSec/filtrar/', login_required(filtrarConfiabilidadesSec.as_view()), name='filtrar_confiabilidadSec'),    
    path('confiabilidad-detalleSec/resultfiltr/', login_required(formResultConfSecfiltr.as_view()), name='form_resultSec_filtr'),    
    path('confiabilidad-muestra-subsistema/', login_required(listarConfSubsitemas.as_view()), name='confiabilidad_muestra_subsistemas'),    
    path('confiabilidad/report-activo-Pr/', login_required(generar_reporte_confiabilidadPrueba.as_view()), name='reporte_confiabilidad_prueba'),    
    path('confiabilidad/report-activo-Sec/', login_required(generar_reporte_confiabilidadPruebaSec.as_view()), name='reporte_confiabilidad_prueba_Sec'),    
    path('confiabilidad/report-activo-PrFltr/', login_required(generar_reporte_confiabilidadPruebaFltr.as_view()), name='reporte_confiabilidad_pruebaFltr'),    
    path('confiabilidad/report-activo-SecFltr/', login_required(generar_reporte_confiabilidadPruebaSecFltr.as_view()), name='reporte_confiabilidad_prueba_SecFltr'),    

    path('fallas/fallas-muestra', login_required(listarFallas.as_view()), name='fallas_muestra'),
    path('fallas/fallas-editar/(?p<pk>\d+)/', login_required(listafallas_editar.as_view()), name='fallas_editar'),
    path('fallas/fallas-eliminar/(?p<pk>\d+)/', login_required(listafallas_eliminar.as_view()), name='fallas_eliminar'),
    
    path('fallas/fallas-equipo-muestra', login_required(listarTiposEquipos.as_view()), name='fallas_equipo_muestra'),
    path('fallas/fallas-equipo-editar/(?p<pk>\d+)/', login_required(listatipoequipo_editar.as_view()), name='fallas_equipo_editar'),
    path('fallas/fallas-equipo-eliminar/(?p<pk>\d+)/', login_required(listatipoequipo_eliminar.as_view()), name='fallas_equipo_eliminar'),
   
    path('fallas/fallas-calificacion', login_required(listarCalificacionFallas.as_view()), name='fallas_calificacion_muestra'),
    path('fallas/fallas-calificaion-editar/(?p<pk>\d+)/', login_required(listacalificacionfallas_editar.as_view()), name='fallas_calificacion_editar'),
    path('fallas/fallas-calificacion-eliminar/(?p<pk>\d+)/', login_required(listacalificacionfallas_eliminar.as_view()), name='fallas_calificacion_eliminar'),
   
    path('fallas/Form-falla', login_required(formularioFalla.as_view()), name='form_falla'),
    path('fallas/Form-Tipo-Equipo', login_required(formularioTipoEquipo.as_view()), name='form_tipo_equipo'),
    path('fallas/Form-Calificacion', login_required(formularioCalificaionFalla.as_view()), name='form_calificacion'),
    path('listado_tipos/', vista_listado_tipos, name='vista_listado_tipos'),

    path('activos/report-activo-Pr/', login_required(generar_reporte_equipoPr.as_view()), name='generar_reporte_equipoPr'),    
    path('activos/report-activo-Sec/', login_required(generar_reporte_equipoSec.as_view()), name='generar_reporte_equipoSec'),    
    path('activos/report-activo-Pr-total/', login_required(generar_reporte_equipoPr_total.as_view()), name='generar_reporte_equipoPr_total'),    
    path('activos/report-activo-Sec-total/', login_required(generar_reporte_equipoSec_total.as_view()), name='generar_reporte_equipoSec_total'),    

    path('activos/report-subsistema/', login_required(generar_reporte_subsistemas.as_view()), name='generar_reporte_subsistemas'),    
    path('activos/report-subsistemas-completo/',reporte_listado_subsistemas, name='reporte_listado_subsistemas'),    

    path('activos/report-sistema/', login_required(generar_reporte_sistemas.as_view()), name='generar_reporte_sistemas'),    
    path('activos/report-sistemas-completo/',reporte_listado_sistemas, name='reporte_listado_sistemas'),    

    path('activos/report-planta-Sec/', login_required(generar_reporte_plantas_secundarias.as_view()), name='generar_reporte_plantas_secundarias'),    
    path('activos/report-planta-completo/',reporte_listado_plantas_secundarias, name='reporte_listado_plantas_secundarias'),  

    path('activos/report-plantas/', login_required(generar_reporte_plantas.as_view()), name='generar_reporte_plantas'),    
    path('activos/report-plantaPr-completo/',reporte_listado_plantas, name='reporte_listado_plantas'),  
    #path('activos/report-activo-Sec-total/', login_required(generar_reporte_equipoSec_total.as_view()), name='generar_reporte_equipoSec_total'),    

    path('activos/report-tipos/', login_required(generar_reporte_tiposEquipoPr.as_view()), name='generar_reporte_tipos'),    
    path('activos/report-tiposSec/',reporte_listado_tiposEquipoSec, name='reporte_listado_tipos'),  

    path('Configuracion-reportes', login_required(formularioConfigReporte.as_view()), name='configReporte'),
    path('Configuracion-reportes/(?p<pk>\d+)/', login_required(editar_formConfigReporte.as_view()), name='configReporte_editar'),

    path('listado_configreport/', vista_listado_configReport, name='vista_listado_configReport'),
    path('confiabilidad-detalle-subsistema',login_required(listarConfiabilidades_subsistema.as_view()), name='conf_detalle_subsistema'),


]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


