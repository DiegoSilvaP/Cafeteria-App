# Generated by Django 3.0.1 on 2020-01-05 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200105_0145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Título de la página de contacto', 'verbose_name_plural': 'Títulos de la página de contacto'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='content',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='subtitle',
        ),
    ]