from django import forms
from .models import *


class FormularioTipoEquipo(forms.ModelForm):
    class Meta:
        model = TipoDeEquipo
        fields = [
            'nombre',
            'falla',
        ]
        labels = {
            'nombre':'Nombre',
            'falla':'Falla',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'id':'nombre','class':'form-control','placeholder':'Tipo Equipo'}),
            'falla': forms.CheckboxSelectMultiple(),
        }

class FormularioFalla(forms.ModelForm):
    class Meta:
        model = Falla
        fields = [
            'codigo',
            'descripcion',
            'calificacion',
        ]
        labels = {
            'codigo':'Código',
            'descripcion':'Descripción',
            'calificacion':'Calificación de Falla',
        }

        widgets = {
            'codigo':forms.TextInput(attrs={'id':'nombre','class':'form-control','placeholder':'Código'}),
            'descripcion': forms.TextInput(attrs={'id':'falla','class':'form-control','placeholder':'Descripción'}),
            'calificacion': forms.Select(attrs={'id':'calif','class':'form-control','placeholder':'Calificación de Falla'}),
        
        }

class FormularioCalificacionFalla(forms.ModelForm):
    class Meta:
        model = CalificacionFalla
        fields = [
            'descripcion',
        ]
        labels = {
            'calificacion':'Calificación de Falla',
        }

        widgets = {
            'descripcion': forms.TextInput(attrs={'id':'descripcion','class':'form-control','placeholder':'Calificación de Falla'}),      
        }