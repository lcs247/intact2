from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def validate_image_extension(logo):
  import os
  ext = os.path.splitext(logo.name)[1]
  valid_extensions = ['.jpg','.png','.jpeg']
  if not ext in valid_extensions:
    raise ValidationError(u'Formato de imagen no válida. Seleccione un archivo de extensión ".jpg",".png" o ".jpeg"')

class ConfiguracionReporte(models.Model):
    logo = models.FileField('Logo de Empresa',upload_to='logos/',validators=[validate_image_extension], blank=True, null=True,default='logotipo')
    empresa = models.CharField('Nombre de Empresa', max_length=70, blank=True)
    direccion = models.CharField('Dirección de Empresa', max_length=70, blank=True)
    email = models.CharField('E-mail de Empresa', max_length=70, blank=True)
    clave = models.CharField('Clave Maestra', max_length=70, blank=True)
