# Generated by Django 3.0.1 on 2020-01-05 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='content',
            field=models.TextField(blank=True, verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subtitle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Subtítulo'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Título'),
        ),
    ]