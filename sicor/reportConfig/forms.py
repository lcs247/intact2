from django import forms
from .models import ConfiguracionReporte

class FormularioConfigReporte(forms.ModelForm):
    class Meta:
        model = ConfiguracionReporte
        fields = [
            'logo',
            'empresa',
            'direccion',
            'email',
            'clave',
        ]
        labels = {
            'logo':'Logo de Empresa',
            'empresa':'Nombre de Empresa',
            'direccion':'Dirección de Empresa',
            'email':'E-mail de Empresa',
            'clave':'Clave Maestra',
        }

        widgets = {
            'empresa':forms.TextInput(attrs={'id':'empres','class':'form-control','placeholder':'Nombre de la Empresa'}),           
            'direccion': forms.TextInput(attrs={'id':'direccion','class':'form-control','placeholder':'Dirección de Empresa'}),
            'email': forms.TextInput(attrs={'id':'e-mail','class':'form-control','placeholder':'e-mail'}),
            'clave': forms.TextInput(attrs={'id':'clave','type':'password','class':'form-control','placeholder':'********'}),
        }