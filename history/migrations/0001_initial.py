# Generated by Django 3.0.1 on 2020-01-05 07:21

from django.db import migrations, models
import history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=history.models.custom_upload_to, verbose_name='Imagen')),
                ('header', models.CharField(blank=True, max_length=150, verbose_name='Encabezado del cover')),
                ('paragraph', models.TextField(blank=True, verbose_name='Párrafor del cover')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name_plural': 'Cover',
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Título de la historia')),
                ('subtitle', models.CharField(max_length=250, verbose_name='Subtítulo')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
            ],
            options={
                'verbose_name_plural': 'History',
            },
        ),
    ]
