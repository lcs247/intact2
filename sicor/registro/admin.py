from django.contrib import admin
from registro.models import Equipo, EquipoPrincipal, PlantaSecundaria,Sistema,Planta, SubSistema

# Register your models here.

class RegEquipo (admin.ModelAdmin):
    list_display = ["nombre","sistema","planta","estado_operativo","codigo_total","datasheet"]
    list_filter = ["planta","sistema","estado"]
    search_fields = ["codigo","nombre","codes"]
    #list_editable =["inscripcion"]
    # fieldsets=(
    #     (None,{
    #         'fields':('planta','sistema','nombre','codigo','estado',)
    #     }),
    #     ('Más opciones',{
    #         'classes':('collapse','wide','extrapretty'),
    #         'fields':('año','capacidad','fu_mantenimiento','observaciones',)
    #     })
    # )
    # def cod(self,obj):
    #     return obj.codes.upper()
    # cod.short_description="CÓDIGO ÚNICO"
    # cod.admin_order_field="codes"

class RegEquipoPrincipal (admin.ModelAdmin):
    list_display = ["nombre","sistema","planta","estado_operativo","codigo_total","datasheet","ingresado","modificado"]
    list_filter = ["planta","sistema","estado"]
    search_fields = ["codigo","nombre","codes"]
    
class RegSistema (admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]

class RegSubsistema (admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]

class RegPlanta (admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]

class RegPlantaSecundaria (admin.ModelAdmin):
    list_display = ["nombre","codigo","descripcion"]
  

admin.site.register(Equipo,RegEquipo)
admin.site.register(EquipoPrincipal,RegEquipoPrincipal)
admin.site.register(Sistema,RegSistema)
admin.site.register(SubSistema,RegSubsistema)
admin.site.register(Planta,RegPlanta)
admin.site.register(PlantaSecundaria,RegPlantaSecundaria)
