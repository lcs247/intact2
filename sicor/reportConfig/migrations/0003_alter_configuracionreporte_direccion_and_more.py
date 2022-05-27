# Generated by Django 4.0 on 2022-05-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reportConfig', '0002_alter_configuracionreporte_clave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuracionreporte',
            name='direccion',
            field=models.CharField(blank=True, max_length=70, verbose_name='Dirección de Empresa'),
        ),
        migrations.AlterField(
            model_name='configuracionreporte',
            name='email',
            field=models.CharField(blank=True, max_length=70, verbose_name='E-mail de Empresa'),
        ),
        migrations.AlterField(
            model_name='configuracionreporte',
            name='empresa',
            field=models.CharField(blank=True, max_length=70, verbose_name='Nombre de Empresa'),
        ),
    ]