from django import forms
from .models import Equipo, Sistema, Planta, PlantaSecundaria, SubSistema, EquipoPrincipal

#PLANTA PRINCIPAL Y SECUNDARIA

class FormularioPlanta(forms.ModelForm):
    class Meta:
        model = Planta
        fields = [
            'nombre',
            'codigo',
            'descripcion',
            'capacidad',
        ]
        labels = {
            'nombre':'Planta',
            'codigo':'Código',
            'descripcion':'Descripción',
            'capacidad':'Capacidad',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'id':'nombre_p','class':'form-control','placeholder':'Planta'}),
            'codigo': forms.TextInput(attrs={'id':'codigo1','class':'form-control','placeholder':'Código 1'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
            'capacidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Capacidad'}),
        }
class FormularioPlantaSecundaria(forms.ModelForm):
    class Meta:
        model = PlantaSecundaria
        fields = [
            'nombre',
            'codigo',
            'descripcion',
            'capacidad',
        ]
        labels = {
            'nombre':'Planta',
            'codigo':'Código',
            'descripcion':'Descripción',
            'capacidad':'Capacidad',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'id':'nombre_p','class':'form-control','placeholder':'Planta'}),
            'codigo': forms.TextInput(attrs={'id':'codigo1','class':'form-control','placeholder':'Código 1'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
            'capacidad': forms.TextInput(attrs={'class':'form-control','placeholder':'Capacidad'}),
        }

#SISTEMA Y SUBSISTEMA

class FormularioSistema(forms.ModelForm):
    class Meta:
        model = Sistema
        fields = [
            'nombre',
            'codigo',
            'descripcion',
        ]
        labels = {
            'nombre':'Sistema',
            'codigo':'Código',
            'descripcion':'Descripción',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'id':'nombre_s','class':'form-control','placeholder':'Sistema'}),
            'codigo': forms.TextInput(attrs={'id':'codigo2','class':'form-control','placeholder':'Código 2'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
        }

class FormularioSubSistema(forms.ModelForm):
    class Meta:
        model = SubSistema
        fields = [
            'nombre',
            'codigo',
            'descripcion',
        ]
        labels = {
            'nombre':'Sistema',
            'codigo':'Código',
            'descripcion':'Descripción',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'id':'nombre_s','class':'form-control','placeholder':'SubSistema'}),
            'codigo': forms.TextInput(attrs={'id':'codigo2','class':'form-control','placeholder':'Código 2'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control','placeholder':'Descripción'}),
        }

#EQUIPO PRINCIPAL Y SECUNDARIO

class FormularioEquipoPrincipal(forms.ModelForm):
    class Meta:
        model = EquipoPrincipal
        fields = [
            'planta',
            'planta_secundaria',
            'sistema',
            'subsistema',
            'codigo',
            'nombre',
            'marca',
            'modelo',
            'serie',
            'tipo',
            'codigo_de_activo',
            'año',
            'capacidad',
            'potencia',
            'presion',
            'producto',
            'temperatura_e',
            'temperatura_s',
            'voltaje',
            'fases',
            'datasheet',
            'fu_mantenimiento',
            'estado',
            'codes',
            'observaciones',
        ]
        labels = {
            'planta':'Planta Principal',
            'planta_secundaria':'Planta Secundaria',
            'sistema':'Sistema',
            'subsistema':'Sub-Sistema',
            'codigo':'Código',
            'nombre':'Nombre',
            'marca':'Marca',
            'modelo':'Modelo',
            'serie':'Serie',
            'tipo':'Tipo',
            'codigo_de_activo':'Código de activo',
            'año':'Fecha de instalación',
            'capacidad':'Capacidad de Diseño/Operativa',
            'potencia':'Potencia',
            'presion':'Presión',
            'producto':'Producto',
            'temperatura_e':'Temperatura de Entrada',
            'temperatura_s':'Temperatura de Salida',
            'voltaje':'Voltaje',
            'fases':'Nro. de Fases',
            'datasheet':'Datasheet',
            'fu_mantenimiento':'Fecha de último mantenimiento integral',
            'estado':'Estado Operativo',
            'codes':'Código Único',
            'observaciones':'Observaciones',
        }

        widgets = {
            'planta':forms.Select(attrs={'id':'plant','class':'form-control','placeholder':'Planta Principal'}),
            'planta_secundaria':forms.Select(attrs={'id':'plantsec','class':'form-control','placeholder':'Planta Secundaria'}),
            'sistema':forms.Select(attrs={'id':'sist','class':'form-control','placeholder':'Sistema'}),
            'subsistema':forms.Select(attrs={'id':'subsist','class':'form-control','placeholder':'Sub-Sistema'}),
            'codigo': forms.TextInput(attrs={'id':'codigo1','class':'form-control','placeholder':'Código de equipo'}),
            'nombre':forms.TextInput(attrs={'id':'nombre_p','class':'form-control','placeholder':'Nombre del equipo'}),           
            'marca': forms.TextInput(attrs={'id':'marca','class':'form-control','placeholder':'Marca'}),
            'modelo': forms.TextInput(attrs={'id':'modelo','class':'form-control','placeholder':'Modelo'}),
            'serie': forms.TextInput(attrs={'id':'serie','class':'form-control','placeholder':'Serie'}),
            'tipo': forms.Select(attrs={'id':'tipo','class':'form-control','placeholder':'Tipo'}),
            'codigo_de_activo': forms.TextInput(attrs={'id':'codigo_activo','class':'form-control','placeholder':'Código de activo'}),
            'año':forms.DateInput(attrs={'type':'date','class':'form-control','placeholder':'Fecha de instalación (dd/mm/aa)'}),
            'capacidad':forms.TextInput(attrs={'id':'cap','class':'form-control','placeholder':'Capacidad de Diseño/Operativa'}),
            'potencia': forms.TextInput(attrs={'id':'potencia','class':'form-control','placeholder':'Potencia'}),           
            'presion': forms.TextInput(attrs={'id':'presion','class':'form-control','placeholder':'Presión descarga'}),           
            'producto': forms.TextInput(attrs={'id':'producto','class':'form-control','placeholder':'Producto'}),           
            'temperatura_e': forms.TextInput(attrs={'id':'temp','class':'form-control','placeholder':'Temperatura de Entrada'}),           
            'temperatura_s': forms.TextInput(attrs={'id':'temp_s','class':'form-control','placeholder':'Temperatura de Salida'}),                       
            'voltaje': forms.TextInput(attrs={'id':'voltaje','class':'form-control','placeholder':'Voltaje'}),           
            'fases': forms.TextInput(attrs={'id':'fases','class':'form-control','placeholder':'Nro. de Fases'}),           
            'fu_mantenimiento':forms.DateInput(attrs={'type':'date','class':'form-control','placeholder':'Fecha de último mantenimiento integral (dd/mm/aa)'}),
            'estado':forms.Select(attrs={'id':'est','class':'form-control','placeholder':'Estado Operativo'}),
            'codes':forms.TextInput(attrs={'id':'codes','class':'form-control','title':'hh:mm:ss'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control','placeholder':'Observaciones'}),
        }



class FormularioEquipo(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'planta',
            'planta_secundaria',
            'sistema',
            'subsistema',
            'equipo_principal',
            'codigo',
            'nombre',
            'marca',
            'modelo',
            'serie',
            'tipo',
            'codigo_de_activo',
            'año',
            'capacidad',
            'potencia',
            'presion',
            'producto',
            'temperatura_e',
            'temperatura_s',
            'voltaje',
            'fases',
            'datasheet',
            'fu_mantenimiento',
            'estado',
            'codes',
            'observaciones',
        ]
        labels = {
            'planta':'Planta Principal',
            'planta_secundaria':'Planta Secundaria',
            'sistema':'Sistema',
            'subsistema':'Sub-Sistema',
            'equipo_principal':'Equipo Principal',
            'codigo':'Código',
            'nombre':'Nombre',
            'marca':'Marca',
            'modelo':'Modelo',
            'serie':'Serie',
            'tipo':'Tipo',
            'codigo_de_activo':'Código de activo',
            'año':'Fecha de instalación',
            'capacidad':'Capacidad de Diseño/Operativa',
            'potencia':'Potencia',
            'presion':'Presión',
            'producto':'Producto',
            'temperatura_e':'Temperatura de Entrada',
            'temperatura_s':'Temperatura de Salida',
            'voltaje':'Voltaje',
            'fases':'Nro. de Fases',
            'datasheet':'Datasheet',
            'fu_mantenimiento':'Fecha de último mantenimiento integral',
            'estado':'Estado Operativo',
            'codes':'Código Único',
            'observaciones':'Observaciones',
        }

        widgets = {
            'planta':forms.Select(attrs={'id':'plant','class':'form-control','placeholder':'Planta Principal'}),
            'planta_secundaria':forms.Select(attrs={'id':'plantsec','class':'form-control','placeholder':'Planta Secundaria'}),
            'sistema':forms.Select(attrs={'id':'sist','class':'form-control','placeholder':'Sistema'}),
            'subsistema':forms.Select(attrs={'id':'subsist','class':'form-control','placeholder':'Sub-Sistema'}),
            'equipo_principal':forms.Select(attrs={'id':'eq_prin','class':'form-control','placeholder':'Equipo Principal'}),
            'codigo': forms.TextInput(attrs={'id':'codigo1','class':'form-control','placeholder':'Código de equipo'}),
            'nombre':forms.TextInput(attrs={'id':'nombre_p','class':'form-control','placeholder':'Nombre del equipo'}),           
            'marca': forms.TextInput(attrs={'id':'marca','class':'form-control','placeholder':'Marca'}),
            'modelo': forms.TextInput(attrs={'id':'modelo','class':'form-control','placeholder':'Modelo'}),
            'serie': forms.TextInput(attrs={'id':'serie','class':'form-control','placeholder':'Serie'}),
            'tipo': forms.Select(attrs={'id':'tipo','class':'form-control','placeholder':'Tipo'}),
            'codigo_de_activo': forms.TextInput(attrs={'id':'codigo_activo','class':'form-control','placeholder':'Código de activo'}),
            'año':forms.DateInput(attrs={'type':'date','class':'form-control','placeholder':'Fecha de instalación (dd/mm/aa)'}),
            'capacidad':forms.TextInput(attrs={'id':'cap','class':'form-control','placeholder':'Capacidad de Diseño/Operativa'}),
            'potencia': forms.TextInput(attrs={'id':'potencia','class':'form-control','placeholder':'Potencia'}),           
            'presion': forms.TextInput(attrs={'id':'presion','class':'form-control','placeholder':'Presión descarga'}),           
            'producto': forms.TextInput(attrs={'id':'producto','class':'form-control','placeholder':'Producto'}),           
            'temperatura_e': forms.TextInput(attrs={'id':'temp','class':'form-control','placeholder':'Temperatura de Entrada'}),           
            'temperatura_s': forms.TextInput(attrs={'id':'temp_s','class':'form-control','placeholder':'Temperatura de Salida'}),                       
            'voltaje': forms.TextInput(attrs={'id':'voltaje','class':'form-control','placeholder':'Voltaje'}),           
            'fases': forms.TextInput(attrs={'id':'fases','class':'form-control','placeholder':'Nro. de Fases'}),           
            'fu_mantenimiento':forms.DateInput(attrs={'type':'date','class':'form-control','placeholder':'Fecha de último mantenimiento integral (dd/mm/aa)'}),
            'estado':forms.Select(attrs={'id':'est','class':'form-control','placeholder':'Estado Operativo'}),
            'codes':forms.TextInput(attrs={'id':'codes','class':'form-control','title':'hh:mm:ss'}),
            'observaciones': forms.Textarea(attrs={'class':'form-control','placeholder':'Observaciones'}),
        }


