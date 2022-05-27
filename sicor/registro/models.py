import code
from pyexpat.errors import codes
from tabnanny import verbose
from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from django.utils.html import format_html
from fallas_funcionales.models import *
# Create your models here.
#OPCIONES

ESTADO = [
    ('O','Operativo'),
    ('F','Fuera de Servicio'),
]


# PLANTAS
class Planta(models.Model):
    nombre = models.CharField('Planta', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=15, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    capacidad = models.CharField('Capacidad', max_length=40, blank=True)

    class meta:
        verbose_name = 'Planta Principal'
        verbose_name_plural = 'Plantas Principales'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class PlantaSecundaria(models.Model):
    nombre = models.CharField('Planta', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=15, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    capacidad = models.CharField('Capacidad', max_length=40, blank=True)

    class meta:
        verbose_name = 'Planta Secundaria'
        verbose_name_plural = 'Plantas Secundarias'
        ordering = ['nombre']
    
    def __str__(self):
        return (self.codigo+' - '+self.nombre)


#SISTEMAS
class Sistema(models.Model):
    nombre = models.CharField('Sistema', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=15, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    #planta = models.ManyToManyField(Planta)
    class meta:
        verbose_name = 'Sistema'
        verbose_name_plural = 'Sistemas'
        ordering = ['nombre']
    
    def __str__(self):
        return (self.codigo+' - '+self.nombre)

class SubSistema(models.Model):
    nombre = models.CharField('Sistema', max_length=70, blank=False)
    codigo = models.CharField('Código', max_length=15, blank=False)
    descripcion = models.CharField('Descripción', max_length=70, blank=True)
    #planta = models.ManyToManyField(Planta)
    class meta:
        verbose_name = 'Sub-Sistema'
        verbose_name_plural = 'Sub-Sistemas'
        ordering = ['nombre']
    
    def __str__(self):
        return (self.codigo+' - '+self.nombre)

#ACTIVOS
def validate_file_extension(datasheet):
  import os
  ext = os.path.splitext(datasheet.name)[1]
  valid_extensions = ['.pdf']
  if not ext in valid_extensions:
    raise ValidationError(u'Formato de archivo no válido. Seleccione un archivo de extensión ".pdf"')

class EquipoPrincipal(models.Model):
    #numero = models.IntegerField('Número')
    planta = models.ForeignKey(Planta,on_delete=models.CASCADE)
    planta_name=models.CharField('Nombre Planta Principal', max_length=100, blank=True)
    planta_secundaria = models.ForeignKey(PlantaSecundaria,on_delete=models.CASCADE)
    planta_secundaria_name=models.CharField('Nombre Planta Secundaria', max_length=100, blank=True)
    sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE)
    sistema_name=models.CharField('Nombre Sistema', max_length=100, blank=True)
    subsistema =models.ForeignKey(SubSistema,on_delete=models.CASCADE,blank=True,default='---')
    subsistema_name=models.CharField('Nombre Subsistema', max_length=100, blank=True)
    codigo = models.CharField('Código', max_length=30, blank=False)
    nombre = models.CharField('Nombre', max_length=70, blank=False)
    codes=models.CharField(max_length=70,blank=True,default='????')
    marca = models.CharField('Marca', max_length=20, blank=True,default='-')
    modelo = models.CharField('Modelo', max_length=20, blank=True,default='-')
    serie = models.CharField('Serie', max_length=20, blank=True,default='-')    
    tipo = models.ForeignKey(TipoDeEquipo,on_delete=models.CASCADE,blank=True,null=True)
    tipo_name=models.CharField('Nombre Tipo', max_length=100, blank=True)
    codigo_de_activo= models.CharField('Código de activo', max_length=15, blank=True,default='-')
    año = models.CharField('Fecha de instalación', max_length=20,blank=True,null=True)
    capacidad = models.CharField('Capacidad de Diseño/Operativa', max_length=70, blank=True,default='-')
    potencia= models.CharField('Potencia', max_length=20, blank=True,default='-')
    presion = models.CharField('Presión descarga', max_length=20, blank=True,default='-')
    producto = models.CharField('Producto', max_length=20, blank=True,default='-')
    temperatura_e = models.CharField('Temperatura de Entrada', max_length=20, blank=True,default='-')
    temperatura_s = models.CharField('Temperatura de Salida', max_length=20, blank=True,default='-')
    voltaje = models.CharField('Voltaje', max_length=20, blank=True,default='-')
    fases = models.CharField('Nro. de Fases', max_length=20, blank=True,default='-')
    datasheet = models.FileField('Datasheet',upload_to='',validators=[validate_file_extension], blank=True,null=True)
    fu_mantenimiento = models.CharField('Fecha de último mantenimiento integral', max_length=20,blank=True,null=True)
    estado = models.CharField('Estado Operativo', max_length=9, choices=ESTADO, default='O')
    observaciones = models.CharField('Observaciones', max_length=100, blank=True,default='-')
    ingresado = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modificado = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Equipo Principal'
       verbose_name_plural = 'Equipos Principales'
       ordering = ['codigo']
    
    def __str__(self):
        cadena=self.codigo+" - "+self.nombre
        return cadena

    def estado_operativo(self):
        if self.estado == 'O':
            # return format_html('<span style="background:green;">'+self.estado+'</span>')
            return format_html('<span style="background:green;">OPERATIVO (O)</span>')
        else:
            return format_html('<span style="background:red;">FUERA DE SERVICIO (F)</span>')


    @property
    def codigo_total(self):
        return (self.planta.nombre+' - '+self.planta_secundaria.nombre+' - '+self.sistema.nombre+' - '+self.subsistema.nombre+' - '+self.codigo)

    def save(self):
        self.codes = self.codigo_total
        self.planta_name=self.planta.nombre
        self.planta_secundaria_name=self.planta_secundaria.nombre
        self.sistema_name=self.sistema.nombre
        self.subsistema_name=self.subsistema.nombre
        self.tipo_name=self.tipo.nombre

        super (EquipoPrincipal, self).save()


class Equipo(models.Model):
    #numero = models.IntegerField('Número')
    planta = models.ForeignKey(Planta,on_delete=models.CASCADE)
    planta_name=models.CharField('Nombre Planta', max_length=100, blank=True)
    planta_secundaria = models.ForeignKey(PlantaSecundaria,on_delete=models.CASCADE)
    planta_secundaria_name=models.CharField('Nombre Planta Secundaria', max_length=100, blank=True)
    sistema = models.ForeignKey(Sistema,on_delete=models.CASCADE)
    sistema_name=models.CharField('Nombre Sistema', max_length=100, blank=True)
    subsistema =models.ForeignKey(SubSistema,on_delete=models.CASCADE,blank=True,default='---')
    subsistema_name=models.CharField('Nombre Subsistema', max_length=100, blank=True)
    equipo_principal = models.ForeignKey(EquipoPrincipal,on_delete=models.CASCADE)
    equipo_principal_name=models.CharField('Nombre Subsistema', max_length=100, blank=True)
    codigo = models.CharField('Código', max_length=25, blank=False)
    nombre = models.CharField('Descripción', max_length=70, blank=False)
    codes=models.CharField(max_length=70,blank=True,default='????')
    marca = models.CharField('Marca', max_length=20, blank=True,default='-')
    modelo = models.CharField('Modelo', max_length=20, blank=True,default='-')
    serie = models.CharField('Serie', max_length=20, blank=True,default='-')    
    tipo = models.ForeignKey(TipoDeEquipo,on_delete=models.CASCADE,blank=True,null=True)
    tipo_name=models.CharField('Nombre Tipo', max_length=100, blank=True)
    codigo_de_activo= models.CharField('Código de activo', max_length=25, blank=True,default='-')
    año = models.CharField('Fecha de instalación',max_length=20,blank=True,null=True)
    capacidad = models.CharField('Capacidad de Diseño/Operativa', max_length=70, blank=True,default='-')
    potencia= models.CharField('Potencia', max_length=20, blank=True,default='-')
    presion = models.CharField('Presión descarga', max_length=20, blank=True,default='-')
    producto = models.CharField('Producto', max_length=20, blank=True,default='-')
    temperatura_e = models.CharField('Temperatura de Entrada', max_length=20, blank=True,default='-')
    temperatura_s = models.CharField('Temperatura de Salida', max_length=20, blank=True,default='-')
    voltaje = models.CharField('Voltaje', max_length=20, blank=True,default='-')
    fases = models.CharField('Nro. de Fases', max_length=20, blank=True,default='-')
    datasheet = models.FileField('Datasheet',upload_to='',validators=[validate_file_extension], blank=True,null=True)
    fu_mantenimiento = models.CharField('Fecha de último mantenimiento integral',max_length=20,blank=True,null=True)
    estado = models.CharField('Estado Operativo', max_length=9, choices=ESTADO, default='O')
    observaciones = models.CharField('Observaciones', max_length=100, blank=True,default='-')
    ingresado = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modificado = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Equipo Secuandario'
       verbose_name_plural = 'Equipos Secundarios'
       ordering = ['codigo']
    
    def __str__(self):
        cadena=self.codigo+" - "+self.nombre
        return cadena

    def estado_operativo(self):
        if self.estado == 'O':
            # return format_html('<span style="background:green;">'+self.estado+'</span>')
            return format_html('<span style="background:green;">OPERATIVO (O)</span>')
        else:
            return format_html('<span style="background:red;">FUERA DE SERVICIO (F)</span>')


    @property
    def codigo_total(self):
        return (self.planta.nombre+' - '+self.planta_secundaria.nombre+' - '+self.sistema.nombre+' - '+self.subsistema.nombre+' - '+self.equipo_principal.nombre+' - '+self.codigo)

    def save(self):
        self.codes = self.codigo_total
        self.planta_name=self.planta.nombre
        self.planta_secundaria_name=self.planta_secundaria.nombre
        self.sistema_name=self.sistema.nombre
        self.subsistema_name=self.subsistema.nombre
        self.equipo_principal_name=self.equipo_principal.nombre
        self.tipo_name=self.tipo.nombre

        super (Equipo, self).save()
