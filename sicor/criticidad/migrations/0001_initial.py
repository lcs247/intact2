# Generated by Django 4.0 on 2022-05-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaRiesgo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70, verbose_name='Nombre del grupo')),
                ('into_name', models.CharField(max_length=70, verbose_name='Descripción de Intolerable')),
                ('intolerable', models.PositiveIntegerField(default=400, verbose_name='Umbral para INTOLERABLE')),
                ('alto_name', models.CharField(max_length=70, verbose_name='Descripción de Alto')),
                ('alto', models.PositiveIntegerField(default=200, verbose_name='Umbral para ALTO')),
                ('medio_name', models.CharField(max_length=70, verbose_name='Descripción de Medio')),
                ('medio', models.PositiveIntegerField(default=70, verbose_name='Umbral para MEDIO')),
                ('moderado_name', models.CharField(max_length=70, verbose_name='Descripción de Moderado')),
                ('moderado', models.PositiveIntegerField(default=20, verbose_name='Umbral para MODERADO')),
                ('aceptable_name', models.CharField(max_length=70, verbose_name='Descripción de Aceptable')),
                ('aceptable', models.PositiveIntegerField(default=0, verbose_name='Umbral para ACEPTABLE')),
            ],
        ),
        migrations.CreateModel(
            name='Costo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Exposicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MdA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Ocurrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Perdida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Redundancia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Segysa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=70)),
                ('valor', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CriticidadPr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='????', max_length=70)),
                ('po', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?')),
                ('ps', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN SISTEMA?')),
                ('fua', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?')),
                ('pe', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?')),
                ('sh', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?')),
                ('ma', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?')),
                ('r', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='REDUNDANCIA')),
                ('crit_pacial', models.FloatField(default=0.0, verbose_name='CRITICIDAD PARCIAL')),
                ('eval_redun', models.PositiveIntegerField(default=0.0, verbose_name='EVAL REDUNDANCIA')),
                ('crit_total', models.FloatField(default=0.0, verbose_name='CRITICIDAD TOTAL')),
                ('ingres', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal')),
            ],
        ),
        migrations.CreateModel(
            name='CriticidadCSec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=30)),
                ('nombre', models.CharField(blank=True, default='????', max_length=70)),
                ('locacion', models.CharField(blank=True, max_length=70, verbose_name='LOCACIÓN')),
                ('fallas', models.PositiveIntegerField(blank=True, default=0, verbose_name='NÚMERO DE FALLAS')),
                ('mtbf', models.PositiveIntegerField(blank=True, default=0, verbose_name='MTBF')),
                ('vdr', models.PositiveIntegerField(default=0, verbose_name='VALOR DE RIESGO')),
                ('ctdr', models.CharField(blank=True, max_length=30, verbose_name='CATEGORÍA DE RIESGO')),
                ('ingres', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.equipo')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.categoriariesgo')),
                ('cm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.costo')),
                ('ex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.exposicion')),
                ('md', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.mda')),
                ('ocurrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.ocurrencia')),
                ('pp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.perdida')),
                ('r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.redundancia')),
                ('segysa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.segysa')),
            ],
        ),
        migrations.CreateModel(
            name='CriticidadCPr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(blank=True, max_length=30)),
                ('nombre', models.CharField(blank=True, default='????', max_length=70)),
                ('locacion', models.CharField(blank=True, max_length=70, verbose_name='LOCACIÓN')),
                ('fallas', models.PositiveIntegerField(blank=True, default=0, verbose_name='NÚMERO DE FALLAS')),
                ('mtbf', models.PositiveIntegerField(blank=True, default=0, verbose_name='MTBF')),
                ('vdr', models.PositiveIntegerField(blank=True, default=0, verbose_name='VALOR DE RIESGO')),
                ('ctdr', models.CharField(blank=True, default='???', max_length=30, verbose_name='CATEGORÍA DE RIESGO')),
                ('ingres', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.equipoprincipal')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.categoriariesgo')),
                ('cm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.costo')),
                ('ex', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.exposicion')),
                ('md', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.mda')),
                ('ocurrencia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.ocurrencia')),
                ('pp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.perdida')),
                ('r', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.redundancia')),
                ('segysa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criticidad.segysa')),
            ],
        ),
        migrations.CreateModel(
            name='Criticidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, default='????', max_length=70)),
                ('po', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN PROCESO OPERATIVO PRINCIPAL?')),
                ('ps', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿ES PARTE DE UN SISTEMA?')),
                ('fua', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SE HA PRODUCIDO ALGUNA FALLA EN EL ÚLTIMO AÑO?')),
                ('pe', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN ECONÓMICA?')),
                ('sh', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN A LA SALUD DEL PERSONAL?')),
                ('ma', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='¿SU PÉRDIDA DE FUNCIÓN PUEDE PRODUCIR AFECTACIÓN AL MEDIO AMBIENTE?')),
                ('r', models.PositiveIntegerField(choices=[(1, 'SI'), (0, 'NO')], default=0, verbose_name='REDUNDANCIA')),
                ('crit_pacial', models.FloatField(default=0.0, verbose_name='CRITICIDAD PARCIAL')),
                ('eval_redun', models.PositiveIntegerField(default=0.0, verbose_name='EVAL REDUNDANCIA')),
                ('crit_total', models.FloatField(default=0.0, verbose_name='CRITICIDAD TOTAL')),
                ('ingres', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('modif', models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')),
                ('activo', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='registro.equipo')),
            ],
        ),
    ]