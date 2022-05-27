from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin
from .models import *
from django import forms

class FormularioConfiabilidadPr(forms.ModelForm):
    class Meta:
        model = ConfiabilidadEquipoPr
        fields = [
            'activo',
            'nombre',
            'tipo',
            'inicio_falla',
            'final_falla',
#            'uptime',
#            'downtime',
            'costo',
            'descripcion',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'tipo':'Tipo de Falla',
            'inicio_falla':'Inicio de la Falla',
            'final_falla':'Final de la Falla',
#            'uptime':'Up time',
#            'downtime':'Down time',
            'costo':'Costo',
            'descripcion':'Descripción',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'inicio_falla': forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
            'final_falla':forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
#            'uptime': forms.TextInput(attrs={'class':'form-control'}),
#            'downtime': forms.TextInput(attrs={'class':'form-control'}),
            'costo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Select(attrs={'class':'form-control'}),
          }

class FormularioConfiabilidadSec(forms.ModelForm):
    class Meta:
        model = ConfiabilidadEquipoSec
        fields = [
            'activo',
            'nombre',
            'tipo',
            'inicio_falla',
            'final_falla',
#            'uptime',
#            'downtime',
            'costo',
            'descripcion',
        ]
        labels = {
            'activo':'Activo',
            'nombre':'Nombre',
            'tipo':'Tipo de Falla',
            'inicio_falla':'Inicio de la Falla',
            'final_falla':'Final de la Falla',
#            'uptime':'Up time',
#            'downtime':'Down time',
            'costo':'Costo',
            'descripcion':'Descripción',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv'}),
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'}),
            'inicio_falla': forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
            'final_falla':forms.DateInput(attrs={'class':'form-control','type':'datetime-local'}),
#            'uptime': forms.TextInput(attrs={'class':'form-control'}),
#            'downtime': forms.TextInput(attrs={'class':'form-control'}),
            'costo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Select(attrs={'class':'form-control'}),
          }



class FormResultConfPr(forms.ModelForm):
    class Meta:
        model = ResultadosConfActivo
        fields = [
            'activo',
            'uptime_total',
            'downtime_total',
            'costo_total',
            'n_fallas',
            'años',
            'TTF',
            'MTBF',
            'MTTR',
            'MTTF',
            'T_falla',
            'T_reparacion',
            'CO',
            'DO',
            'Mantenibilidad',
        ]
        labels = {
            'activo':'Nombre del Activo',
            'uptime_total':'Uptime Total',
            'downtime_total':'Downtime Total',
            'costo_total':'Costo Total',
            'n_fallas':'Número de Fallas',
            'años':'Años',
            'TTF':'TTF',
            'MTBF':'MTBF',
            'MTTR':'MTTR',
            'MTTF':'MTTF',
            'T_falla':'Tasa de Falla',
            'T_reparacion':'Tasa de Reparación',
            'CO':'Confiabilidad Operacional',
            'DO':'Disponibilidad Operacional',
            'Mantenibilidad':'Mantenibilidad',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv','readonly': 'readonly'}),
            'uptime_total':forms.TextInput(attrs={'class':'form-control','id':'up','readonly': 'readonly'}),
            'downtime_total':forms.TextInput(attrs={'class':'form-control','id':'down','readonly': 'readonly'}),
            'costo_total':forms.TextInput(attrs={'class':'form-control','id':'costo_total','readonly': 'readonly'}),
            'n_fallas':forms.TextInput(attrs={'class':'form-control','id':'fallas','readonly': 'readonly'}),
            'años':forms.TextInput(attrs={'class':'form-control','id':'años','readonly': 'readonly'}),
            'TTF':forms.TextInput(attrs={'class':'form-control','id':'TTF','readonly': 'readonly'}),
            'MTBF': forms.TextInput(attrs={'class':'form-control','id':'MTBF','readonly': 'readonly'}),
            'MTTR': forms.TextInput(attrs={'class':'form-control','id':'MTTR','readonly': 'readonly'}),
            'MTTF':forms.TextInput(attrs={'class':'form-control','id':'MTTF','readonly': 'readonly'}),
            'T_falla':forms.TextInput(attrs={'class':'form-control','id':'TF','readonly': 'readonly'}),
            'T_reparacion':forms.TextInput(attrs={'class':'form-control','id':'TR','readonly': 'readonly'}),
            'CO':forms.TextInput(attrs={'class':'form-control','id':'CO','readonly': 'readonly'}),
            'DO':forms.TextInput(attrs={'class':'form-control','id':'DO','readonly': 'readonly'}),
            'Mantenibilidad':forms.TextInput(attrs={'class':'form-control','id':'M','readonly': 'readonly'}),
          }
class FormResultConfPrFltr(forms.ModelForm):
    class Meta:
        model = ResultadosConfActivoFltr
        fields = [
            'activo',
            'uptime_total',
            'downtime_total',
            'costo_total',
            'n_fallas',
            'años',
            'TTF',
            'MTBF',
            'MTTR',
            'MTTF',
            'T_falla',
            'T_reparacion',
            'CO',
            'DO',
            'Mantenibilidad',
        ]
        labels = {
            'activo':'Nombre del Activo',
            'uptime_total':'Uptime Total',
            'downtime_total':'Downtime Total',
            'costo_total':'Costo Total',
            'n_fallas':'Número de Fallas',
            'años':'Años',
            'TTF':'TTF',
            'MTBF':'MTBF',
            'MTTR':'MTTR',
            'MTTF':'MTTF',
            'T_falla':'Tasa de Falla',
            'T_reparacion':'Tasa de Reparación',
            'CO':'Confiabilidad Operacional',
            'DO':'Disponibilidad Operacional',
            'Mantenibilidad':'Mantenibilidad',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv','readonly': 'readonly'}),
            'uptime_total':forms.TextInput(attrs={'class':'form-control','id':'up','readonly': 'readonly'}),
            'downtime_total':forms.TextInput(attrs={'class':'form-control','id':'down','readonly': 'readonly'}),
            'costo_total':forms.TextInput(attrs={'class':'form-control','id':'costo_total','readonly': 'readonly'}),
            'n_fallas':forms.TextInput(attrs={'class':'form-control','id':'fallas','readonly': 'readonly'}),
            'años':forms.TextInput(attrs={'class':'form-control','id':'años','readonly': 'readonly'}),
            'TTF':forms.TextInput(attrs={'class':'form-control','id':'TTF','readonly': 'readonly'}),
            'MTBF': forms.TextInput(attrs={'class':'form-control','id':'MTBF','readonly': 'readonly'}),
            'MTTR': forms.TextInput(attrs={'class':'form-control','id':'MTTR','readonly': 'readonly'}),
            'MTTF':forms.TextInput(attrs={'class':'form-control','id':'MTTF','readonly': 'readonly'}),
            'T_falla':forms.TextInput(attrs={'class':'form-control','id':'TF','readonly': 'readonly'}),
            'T_reparacion':forms.TextInput(attrs={'class':'form-control','id':'TR','readonly': 'readonly'}),
            'CO':forms.TextInput(attrs={'class':'form-control','id':'CO','readonly': 'readonly'}),
            'DO':forms.TextInput(attrs={'class':'form-control','id':'DO','readonly': 'readonly'}),
            'Mantenibilidad':forms.TextInput(attrs={'class':'form-control','id':'M','readonly': 'readonly'}),
          }
class FormResultConfSec(forms.ModelForm):
    class Meta:
        model = ResultadosConfActivoSec
        fields = [
            'activo',
            'uptime_total',
            'downtime_total',
            'costo_total',
            'n_fallas',
            'años',
            'TTF',
            'MTBF',
            'MTTR',
            'MTTF',
            'T_falla',
            'T_reparacion',
            'CO',
            'DO',
            'Mantenibilidad',
        ]
        labels = {
            'activo':'Nombre del Activo',
            'uptime_total':'Uptime Total',
            'downtime_total':'Downtime Total',
            'costo_total':'Costo Total',
            'n_fallas':'Número de Fallas',
            'años':'Años',
            'TTF':'TTF',
            'MTBF':'MTBF',
            'MTTR':'MTTR',
            'MTTF':'MTTF',
            'T_falla':'Tasa de Falla',
            'T_reparacion':'Tasa de Reparación',
            'CO':'Confiabilidad Operacional',
            'DO':'Disponibilidad Operacional',
            'Mantenibilidad':'Mantenibilidad',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv','readonly': 'readonly'}),
            'uptime_total':forms.TextInput(attrs={'class':'form-control','id':'up','readonly': 'readonly'}),
            'downtime_total':forms.TextInput(attrs={'class':'form-control','id':'down','readonly': 'readonly'}),
            'costo_total':forms.TextInput(attrs={'class':'form-control','id':'costo_total','readonly': 'readonly'}),
            'n_fallas':forms.TextInput(attrs={'class':'form-control','id':'fallas','readonly': 'readonly'}),
            'años':forms.TextInput(attrs={'class':'form-control','id':'años','readonly': 'readonly'}),
            'TTF':forms.TextInput(attrs={'class':'form-control','id':'TTF','readonly': 'readonly'}),
            'MTBF': forms.TextInput(attrs={'class':'form-control','id':'MTBF','readonly': 'readonly'}),
            'MTTR': forms.TextInput(attrs={'class':'form-control','id':'MTTR','readonly': 'readonly'}),
            'MTTF':forms.TextInput(attrs={'class':'form-control','id':'MTTF','readonly': 'readonly'}),
            'T_falla':forms.TextInput(attrs={'class':'form-control','id':'TF','readonly': 'readonly'}),
            'T_reparacion':forms.TextInput(attrs={'class':'form-control','id':'TR','readonly': 'readonly'}),
            'CO':forms.TextInput(attrs={'class':'form-control','id':'CO','readonly': 'readonly'}),
            'DO':forms.TextInput(attrs={'class':'form-control','id':'DO','readonly': 'readonly'}),
            'Mantenibilidad':forms.TextInput(attrs={'class':'form-control','id':'M','readonly': 'readonly'}),
          }
class FormResultConfSecFltr(forms.ModelForm):
    class Meta:
        model = ResultadosConfActivoSecFltr
        fields = [
            'activo',
            'uptime_total',
            'downtime_total',
            'costo_total',
            'n_fallas',
            'años',
            'TTF',
            'MTBF',
            'MTTR',
            'MTTF',
            'T_falla',
            'T_reparacion',
            'CO',
            'DO',
            'Mantenibilidad',
        ]
        labels = {
            'activo':'Nombre del Activo',
            'uptime_total':'Uptime Total',
            'downtime_total':'Downtime Total',
            'costo_total':'Costo Total',
            'n_fallas':'Número de Fallas',
            'años':'Años',
            'TTF':'TTF',
            'MTBF':'MTBF',
            'MTTR':'MTTR',
            'MTTF':'MTTF',
            'T_falla':'Tasa de Falla',
            'T_reparacion':'Tasa de Reparación',
            'CO':'Confiabilidad Operacional',
            'DO':'Disponibilidad Operacional',
            'Mantenibilidad':'Mantenibilidad',
        }

        widgets = {
            'activo':forms.Select(attrs={'class':'form-control','id':'actv','readonly': 'readonly'}),
            'uptime_total':forms.TextInput(attrs={'class':'form-control','id':'up','readonly': 'readonly'}),
            'downtime_total':forms.TextInput(attrs={'class':'form-control','id':'down','readonly': 'readonly'}),
            'costo_total':forms.TextInput(attrs={'class':'form-control','id':'costo_total','readonly': 'readonly'}),
            'n_fallas':forms.TextInput(attrs={'class':'form-control','id':'fallas','readonly': 'readonly'}),
            'años':forms.TextInput(attrs={'class':'form-control','id':'años','readonly': 'readonly'}),
            'TTF':forms.TextInput(attrs={'class':'form-control','id':'TTF','readonly': 'readonly'}),
            'MTBF': forms.TextInput(attrs={'class':'form-control','id':'MTBF','readonly': 'readonly'}),
            'MTTR': forms.TextInput(attrs={'class':'form-control','id':'MTTR','readonly': 'readonly'}),
            'MTTF':forms.TextInput(attrs={'class':'form-control','id':'MTTF','readonly': 'readonly'}),
            'T_falla':forms.TextInput(attrs={'class':'form-control','id':'TF','readonly': 'readonly'}),
            'T_reparacion':forms.TextInput(attrs={'class':'form-control','id':'TR','readonly': 'readonly'}),
            'CO':forms.TextInput(attrs={'class':'form-control','id':'CO','readonly': 'readonly'}),
            'DO':forms.TextInput(attrs={'class':'form-control','id':'DO','readonly': 'readonly'}),
            'Mantenibilidad':forms.TextInput(attrs={'class':'form-control','id':'M','readonly': 'readonly'}),
          }
class FormResultConfSubsistema(forms.ModelForm):
    class Meta:
        model = ResultadosConfSubsistemas
        fields = [
            'subsistema',
            'CO',
            'DO',
            'Mantenibilidad',
        ]
        labels = {
            'subsistema':'Nombre del Subsistema',
            'CO':'Confiabilidad Operacional',
            'DO':'Disponibilidad Operacional',
            'Mantenibilidad':'Mantenibilidad',
        }

        widgets = {
            'subsistema':forms.Select(attrs={'class':'form-control','id':'actv','readonly': 'readonly'}),
            'CO':forms.TextInput(attrs={'class':'form-control','id':'CO','readonly': 'readonly'}),
            'DO':forms.TextInput(attrs={'class':'form-control','id':'DO','readonly': 'readonly'}),
            'Mantenibilidad':forms.TextInput(attrs={'class':'form-control','id':'M','readonly': 'readonly'}),
          }