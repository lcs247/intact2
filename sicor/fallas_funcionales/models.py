from django.db import models

# Create your models here.
class CalificacionFalla(models.Model):
    descripcion = models.CharField('Calificación de la Falla', max_length=20, blank=True)
    class meta:
        verbose_name = 'Calificacion'
        verbose_name_plural = 'Calificaciones'
        ordering = ['descripcion']
    
    def __str__(self):
        return self.descripcion
        
class Falla(models.Model):
    codigo = models.CharField('Código', max_length=10, blank=False)
    descripcion = models.CharField('Descripción', max_length=100, blank=True)
    calificacion=models.ForeignKey(CalificacionFalla,on_delete=models.CASCADE)
    class meta:
        verbose_name = 'Falla'
        verbose_name_plural = 'Fallas'
        ordering = ['descripcion']
    
    def __str__(self):
        return self.descripcion

class TipoDeEquipo(models.Model):
    nombre = models.CharField('Sistema', max_length=70, blank=False)
    falla = models.ManyToManyField(Falla)

    class meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre



