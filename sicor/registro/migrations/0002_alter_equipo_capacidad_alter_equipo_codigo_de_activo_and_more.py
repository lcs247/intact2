# Generated by Django 4.0 on 2022-05-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='capacidad',
            field=models.CharField(blank=True, default='-', max_length=70, verbose_name='Capacidad de Diseño/Operativa'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='codigo_de_activo',
            field=models.CharField(blank=True, default='-', max_length=25, verbose_name='Código de activo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fases',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Nro. de Fases'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marca',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='modelo',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='observaciones',
            field=models.CharField(blank=True, default='-', max_length=100, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='potencia',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Potencia'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='presion',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Presión descarga'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='producto',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='serie',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Serie'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='temperatura_e',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Temperatura de Entrada'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='temperatura_s',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Temperatura de Salida'),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='voltaje',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Voltaje'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='capacidad',
            field=models.CharField(blank=True, default='-', max_length=70, verbose_name='Capacidad de Diseño/Operativa'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='codigo_de_activo',
            field=models.CharField(blank=True, default='-', max_length=15, verbose_name='Código de activo'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='fases',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Nro. de Fases'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='marca',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='modelo',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='observaciones',
            field=models.CharField(blank=True, default='-', max_length=100, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='potencia',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Potencia'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='presion',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Presión descarga'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='producto',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Producto'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='serie',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Serie'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='temperatura_e',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Temperatura de Entrada'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='temperatura_s',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Temperatura de Salida'),
        ),
        migrations.AlterField(
            model_name='equipoprincipal',
            name='voltaje',
            field=models.CharField(blank=True, default='-', max_length=20, verbose_name='Voltaje'),
        ),
    ]