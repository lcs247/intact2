from django.contrib import admin
from .models import *

# Register your models here.

class RegResultadosConfActivo(admin.ModelAdmin):
    ordering=['activo']
    autocomplete_fields=['activo']

admin.site.register(ResultadosConfActivo,RegResultadosConfActivo)