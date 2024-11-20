# Generated by Django 5.1.3 on 2024-11-20 04:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriasCuentasModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre de la categoria')),
                ('descripcion', models.CharField(max_length=100, verbose_name='Descripcion de la categoria')),
                ('persupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Presupuesto')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True)),
                ('usr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('usuario_creacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_creacion_categorias', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usuario_modificacion_categorias', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]