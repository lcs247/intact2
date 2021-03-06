# Generated by Django 4.0 on 2022-05-03 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalificacionFalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=20, verbose_name='Calificación de la Falla')),
            ],
        ),
        migrations.CreateModel(
            name='Falla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10, verbose_name='Código')),
                ('descripcion', models.CharField(blank=True, max_length=100, verbose_name='Descripción')),
                ('calificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fallas_funcionales.calificacionfalla')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=70, verbose_name='Sistema')),
                ('falla', models.ManyToManyField(to='fallas_funcionales.Falla')),
            ],
        ),
    ]
