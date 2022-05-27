from django.contrib import admin
from criticidad.models import *
# Register your models here.


class RegCriticidad (admin.ModelAdmin):
    list_display = ["activo","estado","CTT"]
    #list_filter = ["estado"]
    #search_fields = ["codigo","nombre","codes"]
class RegCriticidadPr (admin.ModelAdmin):
    list_display = ["activo","estado","CTT"]
    #list_filter = ["estado"]
    #search_fields = ["codigo","nombre","codes"]
class RegCriticidadCPr (admin.ModelAdmin):
    list_display = ["activo","vdr","ctdr"]

class RegCriticidadCSec (admin.ModelAdmin):
    list_display = ["activo","vdr","ctdr"]


class RegRedundancia (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegOcurrencia (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegSegysa (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegMdA (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegCosto (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegPerdida (admin.ModelAdmin):
    list_display = ["descripcion","valor"]
class RegExposicion (admin.ModelAdmin):
    list_display = ["descripcion","valor"]


admin.site.register(Criticidad,RegCriticidad)
admin.site.register(CriticidadPr,RegCriticidadPr)
admin.site.register(CriticidadCPr,RegCriticidadCPr)
admin.site.register(CriticidadCSec,RegCriticidadCSec)
admin.site.register(Redundancia,RegRedundancia)
admin.site.register(Ocurrencia,RegOcurrencia)
admin.site.register(Segysa,RegSegysa)
admin.site.register(MdA,RegMdA)
admin.site.register(Costo,RegCosto)
admin.site.register(Perdida,RegPerdida)
admin.site.register(Exposicion,RegExposicion)

