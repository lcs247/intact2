from django import forms
from .models import *
#FORMULARIO CRITICIDAD SIMPLE SECUNDARIA
class FormularioCriticidad(forms.ModelForm):
    class Meta:
        model = Criticidad
        fields = [
            'activo',
            'nombre',
            'po',
            'ps',
            'fua',
            'pe',
            'sh',
            'ma',
            'r',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'po':'¿Es parte de un proceso operativo?',
            'ps':'¿Es parte de un sistema?',
            'fua':'¿Se ha producido alguna una falla en el último año?',
            'pe':'¿Su pérdida de función puede producir afectación económica?',
            'sh':'¿Su pérdida de función puede producir afectación a la salud del personal?',
            'ma':'¿Su pérdida de función puede producir afectación al medio ambiente?',
            'r':'Redundancia',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'po': forms.Select(attrs={'id':'po','class':'form-control','title':'hh:mm:ss'}),
            'ps': forms.Select(attrs={'id':'ps','class':'form-control','title':'hh:mm:ss'}),
            'fua': forms.Select(attrs={'id':'fua','class':'form-control','title':'hh:mm:ss'}),
            'pe': forms.Select(attrs={'id':'pe','class':'form-control','title':'hh:mm:ss'}),
            'sh': forms.Select(attrs={'id':'sh','class':'form-control','title':'hh:mm:ss'}),
            'ma': forms.Select(attrs={'id':'ma','class':'form-control','title':'hh:mm:ss'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control','title':'hh:mm:ss'}),
          }

#FORMULARIO CRITICIDAD SIMPLE PRIMARIA

class FormularioCriticidadPr(forms.ModelForm):
    class Meta:
        model = CriticidadPr
        fields = [
            'activo',
            'nombre',
            'po',
            'ps',
            'fua',
            'pe',
            'sh',
            'ma',
            'r',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'po':'¿Es parte de un proceso operativo?',
            'ps':'¿Es parte de un sistema?',
            'fua':'¿Se ha producido alguna una falla en el último año?',
            'pe':'¿Su pérdida de función puede producir afectación económica?',
            'sh':'¿Su pérdida de función puede producir afectación a la salud del personal?',
            'ma':'¿Su pérdida de función puede producir afectación al medio ambiente?',
            'r':'Redundancia',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'po': forms.Select(attrs={'id':'po','class':'form-control','title':'hh:mm:ss'}),
            'ps': forms.Select(attrs={'id':'ps','class':'form-control','title':'hh:mm:ss'}),
            'fua': forms.Select(attrs={'id':'fua','class':'form-control','title':'hh:mm:ss'}),
            'pe': forms.Select(attrs={'id':'pe','class':'form-control','title':'hh:mm:ss'}),
            'sh': forms.Select(attrs={'id':'sh','class':'form-control','title':'hh:mm:ss'}),
            'ma': forms.Select(attrs={'id':'ma','class':'form-control','title':'hh:mm:ss'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control','title':'hh:mm:ss'}),
          }


#FORMULARIO CRITICIDAD COMPLETA PRIMARIA

class FormularioCriticidadCPr(forms.ModelForm):
    class Meta:
        model = CriticidadCPr
        fields = [
            'tag',
            'activo',
            'nombre',
            'r',
            'fallas',
            'ocurrencia',
            'segysa',
            'md',
            'cm',
            'pp',
            'ex',
            'categoria',
        ]
        labels = {
            'tag':'Tag',
            'activo':'Activo',
            'nombre':'Nombre',
            'r':'Redundancia',
            'fallas':'Nro de Fallas',
            'ocurrencia':'Ocurrencia',
            'segysa':'Seguridad y Salud',
            'md':'Medio Ambiente',
            'cm':'Costo de Mantenimiento',
            'pp':'Pérdida de Producción',
            'ex':'Exposición',
            'categoria':'Categoría',
        }

        widgets = {
            'activo':forms.Select(attrs={'id':'activo','class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control'}),
            'fallas': forms.TextInput(attrs={'id':'id_fallas','class':'form-control','readonly': 'readonly'}),
            'ocurrencia': forms.Select(attrs={'id':'ocurrencia','class':'form-control'}),
            'segysa': forms.Select(attrs={'id':'segysa','class':'form-control'}),
            'md': forms.Select(attrs={'id':'md','class':'form-control'}),
            'cm': forms.Select(attrs={'id':'cm','class':'form-control'}),
            'pp': forms.Select(attrs={'id':'pp','class':'form-control'}),
            'ex': forms.Select(attrs={'id':'ex','class':'form-control'}),
            'categoria': forms.Select(attrs={'id':'cat','class':'form-control'}),

          }

#FORMULARIO CRITICIDAD COMPLETA SECUNDARIA

class FormularioCriticidadCSec(forms.ModelForm):
    class Meta:
        model = CriticidadCSec
        fields = [
            'tag',
            'activo',
            'nombre',
            'r',
            'fallas',
            'ocurrencia',
            'segysa',
            'md',
            'cm',
            'pp',
            'ex',
            'categoria',
        ]
        labels = {
            'tag':'Tag',
            'activo':'Activo',
            'nombre':'Nombre',
            'r':'Redundancia',
            'fallas':'Nro de Fallas',
            'ocurrencia':'Ocurrencia',
            'segysa':'Seguridad y Salud',
            'md':'Medio Ambiente',
            'cm':'Costo de Mantenimiento',
            'pp':'Pérdida de Producción',
            'ex':'Exposición',
            'categoria':'Categoría',

        }

        widgets = {
            'activo':forms.Select(attrs={'id':'activo','class':'form-control'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'r': forms.Select(attrs={'id':'r','class':'form-control'}),
            'fallas': forms.TextInput(attrs={'id':'id_fallas','class':'form-control','readonly': 'readonly'}),
            'ocurrencia': forms.Select(attrs={'id':'ocurrencia','class':'form-control'}),
            'segysa': forms.Select(attrs={'id':'segysa','class':'form-control'}),
            'md': forms.Select(attrs={'id':'md','class':'form-control'}),
            'cm': forms.Select(attrs={'id':'cm','class':'form-control'}),
            'pp': forms.Select(attrs={'id':'pp','class':'form-control'}),
            'ex': forms.Select(attrs={'id':'ex','class':'form-control'}),
            'categoria': forms.Select(attrs={'id':'cat','class':'form-control'}),

          }

#FORMULARIO CONFIGURACIÓN REDUNDANCIA
class FormularioRedundancia(forms.ModelForm):
    class Meta:
        model = Redundancia
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN OCURRENCIA
class FormularioOcurrencia(forms.ModelForm):
    class Meta:
        model = Ocurrencia
        fields = [
            'descripcion',
            'rango_menor',
            'rango_mayor',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'rango_menor':'Rango Menor',
            'rango_mayor':'Rango Mayor',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'rango_menor':forms.TextInput(attrs={'class':'form-control','placeholder':'Límite inferior'}),
            'rango_mayor':forms.TextInput(attrs={'class':'form-control','placeholder':'Límite superior'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN SEGYSA
class FormularioSegysa(forms.ModelForm):
    class Meta:
        model = Segysa
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN MDA
class FormularioMdA(forms.ModelForm):
    class Meta:
        model = MdA
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }
#FORMULARIO CONFIGURACIÓN COSTO
class FormularioCosto(forms.ModelForm):
    class Meta:
        model = Costo
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN PERDIDA
class FormularioPerdida(forms.ModelForm):
    class Meta:
        model = Perdida
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN EXPOSICIÓN
class FormularioExposicion(forms.ModelForm):
    class Meta:
        model = Exposicion
        fields = [
            'descripcion',
            'valor',
        ]
        labels = {
            'descripcion':'Descripción',
            'valor':'Valor',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
          }

#FORMULARIO CONFIGURACIÓN DE CATEGORÍAS
class FormularioCategoria(forms.ModelForm):
    class Meta:
        model = CategoriaRiesgo
        fields = [
            'descripcion',
            'into_name',
            'intolerable',
            'alto_name',
            'alto',
            'medio_name',
            'medio',
            'moderado_name',
            'moderado',
            'aceptable_name',
            'aceptable',
        ]
        labels = {
            'descripcion':'Descripción de la Categoría',
            'into_name':'Descripcion de Intolerable',
            'intolerable':'Intolerable',
            'alto_name':'Descripcion de Alto',
            'alto':'Alto',
            'medio_name':'Descripcion de Medio',
            'medio':'Medio',
            'moderado_name':'Descripcion de Moderado',
            'moderado':'Moderado',
            'aceptable_name':'Descripcion de Aceptable',
            'aceptable':'Aceptable',
        }

        widgets = {
            'descripcion':forms.TextInput(attrs={'class':'form-control'}),
            'into_name':forms.TextInput(attrs={'class':'form-control'}),
            'intolerable':forms.TextInput(attrs={'class':'form-control'}),
            'alto_name':forms.TextInput(attrs={'class':'form-control'}),
            'alto':forms.TextInput(attrs={'class':'form-control'}),
            'medio_name':forms.TextInput(attrs={'class':'form-control'}),
            'medio':forms.TextInput(attrs={'class':'form-control'}),
            'moderado_name':forms.TextInput(attrs={'class':'form-control'}),
            'moderado':forms.TextInput(attrs={'class':'form-control'}),
            'aceptable_name':forms.TextInput(attrs={'class':'form-control'}),
            'aceptable':forms.TextInput(attrs={'class':'form-control'}),
          }

