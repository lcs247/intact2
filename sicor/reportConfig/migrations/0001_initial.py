# Generated by Django 4.0 on 2022-05-12 19:24

from django.db import migrations, models
import reportConfig.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionReporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to='./static/logos/', validators=[reportConfig.models.validate_image_extension], verbose_name='Logo de Empresa')),
                ('empresa', models.CharField(blank=True, default='-', max_length=70, verbose_name='Nombre de Empresa')),
                ('direccion', models.CharField(blank=True, default='-', max_length=70, verbose_name='Dirección de Empresa')),
                ('email', models.CharField(blank=True, default='-', max_length=70, verbose_name='E-mail de Empresa')),
                ('clave', models.CharField(blank=True, default='-', max_length=70, verbose_name='Clave Maestra')),
            ],
        ),
    ]
