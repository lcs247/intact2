from django.db import models
from registro.models import *
from fallas_funcionales.models import *
#from datetime import datetime

# Create your models here.
ESTADO = [
    ('Programado','Programado'),
    ('No Programado','No Programado'),
]
#CONFIABILIDAD//////////////////////////////////////////////////////////////////////////////////////////
#PRINCIPALES
class ConfiabilidadEquipoPr(models.Model):
    activo = models.ForeignKey(EquipoPrincipal,on_delete=models.CASCADE)
    sistema=models.CharField(max_length=10,blank=True,default='????')
    subsistema=models.CharField(max_length=10,blank=True,default='????')
    planta_principal=models.CharField(max_length=10,blank=True,default='????')
    planta_secundaria=models.CharField(max_length=10,blank=True,default='????')
    nombre=models.CharField(max_length=70,blank=True,default='????')
    inicio_falla = models.CharField('Inicio de la Falla',max_length=70,blank=True,null=True)
    final_falla = models.CharField('Final de la Falla',max_length=70,blank=True,null=True)
#    uptime=models.FloatField('Up time', default=0, blank=False)
    downtime =models.FloatField('Down time', default=0, blank=False)
    costo=models.FloatField('Costo', default=0, blank=False)
    descripcion=models.CharField('Descripción',max_length=100,blank=True)
    tipo=models.CharField('Tipo de Falla', max_length=13, choices=ESTADO, default='No Programado')
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

 
    class Meta:
        ordering = ["inicio_falla"]

    @property
    def codigo_total(self):
        return (self.activo.codigo+' - '+self.activo.nombre)

    def save(self):
        self.nombre = self.codigo_total
        self.sistema=self.activo.sistema_id
        self.subsistema=self.activo.subsistema_id
        self.planta_principal=self.activo.planta_id
        self.planta_secundaria=self.activo.planta_secundaria_id

        self.downtime=((datetime.strptime(self.inicio_falla, "%Y-%m-%dT%H:%M")-datetime.strptime(self.final_falla, "%Y-%m-%dT%H:%M")).total_seconds()*(-1))/(86400)
        super (ConfiabilidadEquipoPr, self).save()
#SECUNDARIOS
class ConfiabilidadEquipoSec(models.Model):
    activo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    equipo_pr=models.CharField(max_length=10,blank=True,default='????')
    sistema=models.CharField(max_length=10,blank=True,default='????')
    subsistema=models.CharField(max_length=10,blank=True,default='????')
    planta_principal=models.CharField(max_length=10,blank=True,default='????')
    planta_secundaria=models.CharField(max_length=10,blank=True,default='????')
    nombre=models.CharField(max_length=70,blank=True,default='????')
    inicio_falla = models.CharField('Inicio de la Falla',max_length=70,blank=True,null=True)
    final_falla = models.CharField('Final de la Falla',max_length=70,blank=True,null=True)
#    uptime=models.FloatField('Up time', default=0, blank=False)
    downtime =models.FloatField('Down time', default=0, blank=False)
    costo=models.FloatField('Costo', default=0, blank=False)
    descripcion=models.CharField('Descripción',max_length=100,blank=True)
    tipo=models.CharField('Tipo de Falla', max_length=13, choices=ESTADO, default='No Programado')
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class Meta:
        ordering = ["inicio_falla"]

    @property
    def codigo_total(self):
        return (self.activo.codigo+' - '+self.activo.nombre)

    def save(self):
        self.nombre = self.codigo_total
        self.equipo_pr=self.activo.equipo_principal_id
        self.sistema=self.activo.sistema_id
        self.subsistema=self.activo.subsistema_id
        self.planta_principal=self.activo.planta_id
        self.planta_secundaria=self.activo.planta_secundaria_id
        self.downtime=((datetime.strptime(self.inicio_falla, "%Y-%m-%dT%H:%M")-datetime.strptime(self.final_falla, "%Y-%m-%dT%H:%M")).total_seconds()*(-1))/(86400)
        super (ConfiabilidadEquipoSec, self).save()
#GUARDAR RESULTADOS DE CONFIABILIDAD///////////////////////////////////////////////////////////////////////
#PRINCIPAL////////////////////////////////////////////////////////////////////////////////
class ResultadosConfActivo(models.Model):
    activo = models.ForeignKey(EquipoPrincipal,on_delete=models.CASCADE)
    uptime_total= models.FloatField('Up time', default=0, blank=False)
    downtime_total=models.FloatField('Downtime time', default=0, blank=False)
    costo_total=models.FloatField('Costo', default=0, blank=False)
    n_fallas=models.FloatField('Número de fallas', default=0, blank=False)
    años=models.FloatField('Años', default=0, blank=False)
    TTF=models.FloatField('TTF', default=0, blank=False)
    MTBF=models.FloatField('MTBF', default=0, blank=False)
    MTTR=models.FloatField('MTTR', default=0, blank=False)
    MTTF=models.FloatField('MTTF', default=0, blank=False)
    T_falla=models.FloatField('Tasa de falla', default=0, blank=False)
    T_reparacion=models.FloatField('Tasa de reparación', default=0, blank=False)
    CO=models.FloatField('Confiabilidad Operacional', default=0, blank=False)
    DO=models.FloatField('Disponibilidad Operacional', default=0, blank=False)
    Mantenibilidad=models.FloatField('Mantenibilidad', default=0, blank=False)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)
#SECUNDARIO/////////////////////////////////////////////////////////////////////////////////
class ResultadosConfActivoSec(models.Model):
    activo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    uptime_total= models.FloatField('Up time', default=0, blank=False)
    downtime_total=models.FloatField('Downtime time', default=0, blank=False)
    costo_total=models.FloatField('Costo', default=0, blank=False)
    n_fallas=models.FloatField('Número de fallas', default=0, blank=False)
    años=models.FloatField('Años', default=0, blank=False)
    TTF=models.FloatField('TTF', default=0, blank=False)
    MTBF=models.FloatField('MTBF', default=0, blank=False)
    MTTR=models.FloatField('MTTR', default=0, blank=False)
    MTTF=models.FloatField('MTTF', default=0, blank=False)
    T_falla=models.FloatField('Tasa de falla', default=0, blank=False)
    T_reparacion=models.FloatField('Tasa de reparación', default=0, blank=False)
    CO=models.FloatField('Confiabilidad Operacional', default=0, blank=False)
    DO=models.FloatField('Disponibilidad Operacional', default=0, blank=False)
    Mantenibilidad=models.FloatField('Mantenibilidad', default=0, blank=False)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

#GUARDAR RESULTADOS DE CONFIABILIDAD FILTRADA///////////////////////////////////////////////////////////////////////
#PRINCIPAL///////////////////////////////////////////////////////////////////////////////////////
class ResultadosConfActivoFltr(models.Model):
    activo = models.ForeignKey(EquipoPrincipal,on_delete=models.CASCADE)
    uptime_total= models.FloatField('Up time', default=0, blank=False)
    downtime_total=models.FloatField('Downtime time', default=0, blank=False)
    costo_total=models.FloatField('Costo', default=0, blank=False)
    n_fallas=models.FloatField('Número de fallas', default=0, blank=False)
    años=models.FloatField('Años', default=0, blank=False)
    TTF=models.FloatField('TTF', default=0, blank=False)
    MTBF=models.FloatField('MTBF', default=0, blank=False)
    MTTR=models.FloatField('MTTR', default=0, blank=False)
    MTTF=models.FloatField('MTTF', default=0, blank=False)
    T_falla=models.FloatField('Tasa de falla', default=0, blank=False)
    T_reparacion=models.FloatField('Tasa de reparación', default=0, blank=False)
    CO=models.FloatField('Confiabilidad Operacional', default=0, blank=False)
    DO=models.FloatField('Disponibilidad Operacional', default=0, blank=False)
    Mantenibilidad=models.FloatField('Mantenibilidad', default=0, blank=False)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)
#SECUNDARIO///////////////////////////////////////////////////////////////////////////////////////
class ResultadosConfActivoSecFltr(models.Model):
    activo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    uptime_total= models.FloatField('Up time', default=0, blank=False)
    downtime_total=models.FloatField('Downtime time', default=0, blank=False)
    costo_total=models.FloatField('Costo', default=0, blank=False)
    n_fallas=models.FloatField('Número de fallas', default=0, blank=False)
    años=models.FloatField('Años', default=0, blank=False)
    TTF=models.FloatField('TTF', default=0, blank=False)
    MTBF=models.FloatField('MTBF', default=0, blank=False)
    MTTR=models.FloatField('MTTR', default=0, blank=False)
    MTTF=models.FloatField('MTTF', default=0, blank=False)
    T_falla=models.FloatField('Tasa de falla', default=0, blank=False)
    T_reparacion=models.FloatField('Tasa de reparación', default=0, blank=False)
    CO=models.FloatField('Confiabilidad Operacional', default=0, blank=False)
    DO=models.FloatField('Disponibilidad Operacional', default=0, blank=False)
    Mantenibilidad=models.FloatField('Mantenibilidad', default=0, blank=False)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

#GUARDAR RESULTADOS DE CONFIABILIDAD GRUPAL///////////////////////////////////////////////////////////////////////
#SUBSISTEMAS//////////////////////////////////////////////////////////////////////
class ResultadosConfSubsistemas(models.Model):
    subsistema = models.ForeignKey(SubSistema,on_delete=models.CASCADE)
    CO=models.FloatField('Confiabilidad Operacional', default=0, blank=False)
    DO=models.FloatField('Disponibilidad Operacional', default=0, blank=False)
    Mantenibilidad=models.FloatField('Mantenibilidad', default=0, blank=False)
