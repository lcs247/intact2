# Generated by Django 4.0 on 2022-05-03 00:01

from django.db import migrations, models
import django.db.models.deletion
import registro.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fallas_funcionales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Planta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Planta')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código')),
                ('descripcion', models.CharField(blank=True, max_length=70, verbose_name='Descripción')),
                ('capacidad', models.CharField(blank=True, max_length=40, verbose_name='Capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='PlantaSecundaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Planta')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código')),
                ('descripcion', models.CharField(blank=True, max_length=70, verbose_name='Descripción')),
                ('capacidad', models.CharField(blank=True, max_length=40, verbose_name='Capacidad')),
            ],
        ),
        migrations.CreateModel(
            name='Sistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Sistema')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código')),
                ('descripcion', models.CharField(blank=True, max_length=70, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='SubSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Sistema')),
                ('codigo', models.CharField(max_length=15, verbose_name='Código')),
                ('descripcion', models.CharField(blank=True, max_length=70, verbose_name='Descripción')),
            ],
        ),
        migrations.CreateModel(
            name='EquipoPrincipal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=30, verbose_name='Código')),
                ('nombre', models.CharField(max_length=70, verbose_name='Nombre')),
                ('codes', models.CharField(blank=True, default='????', max_length=70)),
                ('marca', models.CharField(blank=True, max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=20, verbose_name='Modelo')),
                ('serie', models.CharField(blank=True, max_length=20, verbose_name='Serie')),
                ('codigo_de_activo', models.CharField(blank=True, max_length=15, verbose_name='Código de activo')),
                ('año', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fecha de instalación')),
                ('capacidad', models.CharField(blank=True, max_length=70, verbose_name='Capacidad de Diseño/Operativa')),
                ('potencia', models.CharField(blank=True, max_length=20, verbose_name='Potencia')),
                ('presion', models.CharField(blank=True, max_length=20, verbose_name='Presión descarga')),
                ('producto', models.CharField(blank=True, max_length=20, verbose_name='Producto')),
                ('temperatura_e', models.CharField(blank=True, max_length=20, verbose_name='Temperatura de Entrada')),
                ('temperatura_s', models.CharField(blank=True, max_length=20, verbose_name='Temperatura de Salida')),
                ('voltaje', models.CharField(blank=True, max_length=20, verbose_name='Voltaje')),
                ('fases', models.CharField(blank=True, max_length=20, verbose_name='Nro. de Fases')),
                ('datasheet', models.FileField(blank=True, null=True, upload_to='', validators=[registro.models.validate_file_extension], verbose_name='Datasheet')),
                ('fu_mantenimiento', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fecha de último mantenimiento integral')),
                ('estado', models.CharField(choices=[('O', 'Operativo'), ('F', 'Fuera de Servicio')], default='O', max_length=9, verbose_name='Estado Operativo')),
                ('observaciones', models.CharField(blank=True, max_length=100, verbose_name='Observaciones')),
                ('ingresado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.planta')),
                ('planta_secundaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.plantasecundaria')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.sistema')),
                ('subsistema', models.ForeignKey(blank=True, default='---', on_delete=django.db.models.deletion.CASCADE, to='registro.subsistema')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fallas_funcionales.tipodeequipo')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=25, verbose_name='Código')),
                ('nombre', models.CharField(max_length=70, verbose_name='Descripción')),
                ('codes', models.CharField(blank=True, default='????', max_length=70)),
                ('marca', models.CharField(blank=True, max_length=20, verbose_name='Marca')),
                ('modelo', models.CharField(blank=True, max_length=20, verbose_name='Modelo')),
                ('serie', models.CharField(blank=True, max_length=20, verbose_name='Serie')),
                ('codigo_de_activo', models.CharField(blank=True, max_length=25, verbose_name='Código de activo')),
                ('año', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fecha de instalación')),
                ('capacidad', models.CharField(blank=True, max_length=70, verbose_name='Capacidad de Diseño/Operativa')),
                ('potencia', models.CharField(blank=True, max_length=20, verbose_name='Potencia')),
                ('presion', models.CharField(blank=True, max_length=20, verbose_name='Presión descarga')),
                ('producto', models.CharField(blank=True, max_length=20, verbose_name='Producto')),
                ('temperatura_e', models.CharField(blank=True, max_length=20, verbose_name='Temperatura de Entrada')),
                ('temperatura_s', models.CharField(blank=True, max_length=20, verbose_name='Temperatura de Salida')),
                ('voltaje', models.CharField(blank=True, max_length=20, verbose_name='Voltaje')),
                ('fases', models.CharField(blank=True, max_length=20, verbose_name='Nro. de Fases')),
                ('datasheet', models.FileField(blank=True, null=True, upload_to='', validators=[registro.models.validate_file_extension], verbose_name='Datasheet')),
                ('fu_mantenimiento', models.CharField(blank=True, max_length=20, null=True, verbose_name='Fecha de último mantenimiento integral')),
                ('estado', models.CharField(choices=[('O', 'Operativo'), ('F', 'Fuera de Servicio')], default='O', max_length=9, verbose_name='Estado Operativo')),
                ('observaciones', models.CharField(blank=True, max_length=100, verbose_name='Observaciones')),
                ('ingresado', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('equipo_principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal')),
                ('planta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.planta')),
                ('planta_secundaria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.plantasecundaria')),
                ('sistema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.sistema')),
                ('subsistema', models.ForeignKey(blank=True, default='---', on_delete=django.db.models.deletion.CASCADE, to='registro.subsistema')),
                ('tipo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fallas_funcionales.tipodeequipo')),
            ],
        ),
    ]
