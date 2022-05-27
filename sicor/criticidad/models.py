from django.db import models
from registro.models import *
# Create your models here.

#OPCIONES
ESTADO = [
    (1,'SI'),
    (0,'NO'),
]
#CRITICIDAD SIMPLE PARA ACTIVOS PRINCIPALES
class CriticidadPr(models.Model):
    activo = models.OneToOneField(EquipoPrincipal,on_delete=models.CASCADE)
    nombre = models.CharField(max_length=70,blank=True,default='????') 
    po = models.PositiveIntegerField('¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?',choices=ESTADO, default=0, blank=False)
    ps=models.PositiveIntegerField('¿ES PARTE DE UN SISTEMA?',choices=ESTADO, default=0, blank=False)
    fua = models.PositiveIntegerField('¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?',choices=ESTADO, default=0, blank=False)
    pe = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?',choices=ESTADO, default=0, blank=False)
    sh = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?',choices=ESTADO, default=0, blank=False)
    ma = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?',choices=ESTADO, default=0, blank=False)
    r = models.PositiveIntegerField('REDUNDANCIA', choices=ESTADO, default=0, blank=False)
    crit_pacial = models.FloatField('CRITICIDAD PARCIAL',blank=False,default=0.00)
    eval_redun = models.PositiveIntegerField('EVAL REDUNDANCIA',blank=False,default=0.00)
    crit_total = models.FloatField('CRITICIDAD TOTAL',blank=False, default=0.00)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Principal)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    

    @property
    def CT(self):
        return ((self.po*20)+(self.ps*15)+(self.fua*5)+(self.pe*10)+(self.sh*10)+(self.ma*10))

    def save(self):
        if self.r==1:
            self.eval_redun=0
        if self.r==0:
            self.eval_redun=30       
        self.crit_pacial=self.CT
        self.crit_total=(self.crit_pacial+self.eval_redun)*0.05
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'
        super (CriticidadPr, self).save()
    def CTT(self):
        return (self.crit_total)
    def estado(self):
        if self.crit_total >= 0 and self.crit_total<2:
            return format_html('<span style="background:green;"><b>BAJO</span>')
            # return format_html('<span style="background:green;">'+str(self.crit_total)+'</span>')
        if self.crit_total >= 2 and self.crit_total<4:
            return format_html('<span style="background:yellow;color:blue"><b>MEDIO</span>')
        if self.crit_total >= 4 and self.crit_total<=5:
            return format_html('<span style="background:red;"><b>ALTO</span>')

#CRITICIDAD SIMPLE PARA ACTIVOS SECUNDARIOS
class Criticidad(models.Model):
    activo = models.OneToOneField(Equipo,on_delete=models.CASCADE,blank=True)  
    nombre=models.CharField(max_length=70,blank=True,default='????')
    po = models.PositiveIntegerField('¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?',choices=ESTADO, default=0, blank=False)
    ps=models.PositiveIntegerField('¿ES PARTE DE UN SISTEMA?',choices=ESTADO, default=0, blank=False)
    fua = models.PositiveIntegerField('¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?',choices=ESTADO, default=0, blank=False)
    pe = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?',choices=ESTADO, default=0, blank=False)
    sh = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?',choices=ESTADO, default=0, blank=False)
    ma = models.PositiveIntegerField('¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?',choices=ESTADO, default=0, blank=False)
    r = models.PositiveIntegerField('REDUNDANCIA', choices=ESTADO, default=0, blank=False)
    crit_pacial = models.FloatField('CRITICIDAD PARCIAL',blank=False,default=0.00)
    eval_redun = models.PositiveIntegerField('EVAL REDUNDANCIA',blank=False,default=0.00)
    crit_total = models.FloatField('CRITICIDAD TOTAL',blank=False, default=0.00)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Secundaria)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    

    @property
    def CT(self):
        return ((self.po*20)+(self.ps*15)+(self.fua*5)+(self.pe*10)+(self.sh*10)+(self.ma*10))

    def save(self):
        if self.r==1:
            self.eval_redun=0
        if self.r==0:
            self.eval_redun=30       
        self.crit_pacial=self.CT
        self.crit_total=(self.crit_pacial+self.eval_redun)*0.05
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'
        super (Criticidad, self).save()
    def CTT(self):
        return (self.crit_total)
    def estado(self):
        if self.crit_total >= 0 and self.crit_total<2:
            return format_html('<span style="background:green;"><b>BAJO</span>')
            # return format_html('<span style="background:green;">'+str(self.crit_total)+'</span>')
        if self.crit_total >= 2 and self.crit_total<4:
            return format_html('<span style="background:yellow;color:blue"><b>MEDIO</span>')
        if self.crit_total >= 4 and self.crit_total<=5:
            return format_html('<span style="background:red;"><b>ALTO</span>')

#FORMULARIOS DE VALORES PARA CÁLCULO DE LA CRITICIDAD

class Redundancia(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Ocurrencia(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    rango_menor = models.PositiveIntegerField(default=0, blank=False)
    rango_mayor = models.PositiveIntegerField(default=0, blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (str(self.rango_menor)+'≤ Nº. FALLAS ≤'+str(self.rango_mayor)+' ('+str(self.valor)+')')

class Segysa(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class MdA(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Costo(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Perdida(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class Exposicion(models.Model):
    descripcion = models.CharField(max_length=70,blank=False)
    valor = models.PositiveIntegerField(default=0, blank=False)
    def __str__(self):
        return (self.descripcion+' ('+str(self.valor)+')')

class CategoriaRiesgo(models.Model):
    descripcion = models.CharField('Nombre del grupo',max_length=70,blank=False)
    into_name= models.CharField('Descripción de Intolerable',max_length=70,blank=False)
    intolerable = models.PositiveIntegerField('Umbral para INTOLERABLE',default=400, blank=False)
    alto_name= models.CharField('Descripción de Alto',max_length=70,blank=False)
    alto = models.PositiveIntegerField('Umbral para ALTO',default=200, blank=False)
    medio_name= models.CharField('Descripción de Medio',max_length=70,blank=False)
    medio = models.PositiveIntegerField('Umbral para MEDIO',default=70, blank=False)
    moderado_name= models.CharField('Descripción de Moderado',max_length=70,blank=False)
    moderado = models.PositiveIntegerField('Umbral para MODERADO',default=20, blank=False)
    aceptable_name= models.CharField('Descripción de Aceptable',max_length=70,blank=False)
    aceptable = models.PositiveIntegerField('Umbral para ACEPTABLE',default=0, blank=False)

    def __str__(self):
        return (self.descripcion+':'+ self.into_name +'('+str(self.intolerable)+'), '+self.alto_name +'('+str(self.alto)+'), '+self.medio_name+'('+str(self.medio)+'), '+self.moderado_name+'('+str(self.moderado)+'), '+self.aceptable_name+'('+str(self.aceptable)+')')

#CRITICIDAD COMPLETA PARA ACTIVOS PRINCIPALES

class CriticidadCPr(models.Model):
    tag= models.CharField(max_length=30,blank=True)
    activo = models.OneToOneField(EquipoPrincipal,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=70,blank=True,default='????')
    locacion = models.CharField('LOCACIÓN',max_length=70,blank=True) 
    r = models.ForeignKey(Redundancia,on_delete=models.CASCADE)
    fallas=models.PositiveIntegerField('NÚMERO DE FALLAS', blank=True)
    mtbf = models.PositiveIntegerField('MTBF', default=0, blank=True)
    ocurrencia = models.ForeignKey(Ocurrencia,on_delete=models.CASCADE)
    segysa = models.ForeignKey(Segysa,on_delete=models.CASCADE)
    md = models.ForeignKey(MdA,on_delete=models.CASCADE)
    cm = models.ForeignKey(Costo,on_delete=models.CASCADE)
    pp = models.ForeignKey(Perdida,on_delete=models.CASCADE)
    ex= models.ForeignKey(Exposicion,on_delete=models.CASCADE)
    vdr = models.PositiveIntegerField('VALOR DE RIESGO',blank=True,default=0)
    ctdr = models.CharField('CATEGORÍA DE RIESGO',max_length=30,blank=True,default='???')
    categoria= models.ForeignKey(CategoriaRiesgo,on_delete=models.CASCADE)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Principal)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    
    #OCURRENCIA*EXPOSICIÓN*SUMA()
    @property
    def VDR(self):
       return ((self.ocurrencia.valor)*(self.ex.valor)*((self.segysa.valor)+(self.md.valor)+(self.cm.valor)+(self.pp.valor)+(self.r.valor)))
    def save(self):
        self.locacion=self.activo.planta.nombre
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'+' - '+self.locacion
        self.tag=self.activo.codigo
        self.vdr=self.VDR
        if self.vdr>self.categoria.intolerable:
            self.ctdr=self.categoria.into_name
        if self.vdr>self.categoria.alto and self.vdr<=self.categoria.intolerable:
            self.ctdr=self.categoria.alto_name
        if self.vdr>self.categoria.medio and self.vdr<=self.categoria.alto:
            self.ctdr=self.categoria.medio_name
        if self.vdr>self.categoria.moderado and self.vdr<=self.categoria.medio:
            self.ctdr=self.categoria.moderado_name
        if self.vdr<=self.categoria.moderado:
            self.ctdr=self.categoria.aceptable_name
        super (CriticidadCPr, self).save()


#CRITICIDAD COMPLETA PARA ACTIVOS SECUNDARIOS

class CriticidadCSec(models.Model):
    tag= models.CharField(max_length=30,blank=True)
    activo = models.OneToOneField(Equipo,on_delete=models.CASCADE)
    nombre=models.CharField(max_length=70,blank=True,default='????')    
    locacion = models.CharField('LOCACIÓN',max_length=70,blank=True) 
    r = models.ForeignKey(Redundancia,on_delete=models.CASCADE)
    fallas=models.PositiveIntegerField('NÚMERO DE FALLAS', default=0, blank=True)
    mtbf = models.PositiveIntegerField('MTBF', default=0, blank=True)
    ocurrencia = models.ForeignKey(Ocurrencia,on_delete=models.CASCADE)
    segysa = models.ForeignKey(Segysa,on_delete=models.CASCADE)
    md = models.ForeignKey(MdA,on_delete=models.CASCADE)
    cm = models.ForeignKey(Costo,on_delete=models.CASCADE)
    pp = models.ForeignKey(Perdida,on_delete=models.CASCADE)
    ex= models.ForeignKey(Exposicion,on_delete=models.CASCADE)
    vdr = models.PositiveIntegerField('VALOR DE RIESGO',blank=False,default=0)
    ctdr = models.CharField('CATEGORÍA DE RIESGO',max_length=30,blank=True)
    categoria= models.ForeignKey(CategoriaRiesgo,on_delete=models.CASCADE)
    ingres = models.DateTimeField('Fecha de registro',auto_now_add=True,auto_now=False)
    modif = models.DateTimeField('Fecha de modificación',auto_now_add=False,auto_now=True)

    class meta:
       verbose_name = 'Criticidad (Secundaria)'
       verbose_name_plural = 'Criticidades'
       
    # def __str__(self):
    #      return self.activo
    
    #OCURRENCIA*EXPOSICIÓN*SUMA()
    @property
    def VDR(self):
       return ((self.ocurrencia.valor)*(self.ex.valor)*((self.segysa.valor)+(self.md.valor)+(self.cm.valor)+(self.pp.valor)+(self.r.valor)))
    def save(self):
        self.locacion=self.activo.planta.nombre
        self.nombre=self.activo.nombre+' ('+self.activo.codigo+')'+' - '+self.locacion
        self.tag=self.activo.codigo
        self.vdr=self.VDR
        if self.vdr>self.categoria.intolerable:
            self.ctdr=self.categoria.into_name
        if self.vdr>self.categoria.alto and self.vdr<=self.categoria.intolerable:
            self.ctdr=self.categoria.alto_name
        if self.vdr>self.categoria.medio and self.vdr<=self.categoria.alto:
            self.ctdr=self.categoria.medio_name
        if self.vdr>self.categoria.moderado and self.vdr<=self.categoria.medio:
            self.ctdr=self.categoria.moderado_name
        if self.vdr<=self.categoria.moderado:
            self.ctdr=self.categoria.aceptable_name
        super (CriticidadCSec, self).save()
