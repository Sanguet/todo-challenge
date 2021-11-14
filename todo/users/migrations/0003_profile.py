# Generated by Django 3.1 on 2021-11-13 19:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20211113_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date Time de la creacion del objeto', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date Time de la ultima modificacion del objeto', verbose_name='modified at')),
                ('is_active', models.BooleanField(blank=True, default=True, help_text='La fila esta activa o no', verbose_name='is active')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='users/pictures/', verbose_name='imagen de perfil')),
                ('first_name', models.CharField(max_length=30, verbose_name='Nombre del perfil')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido del perfil')),
                ('country', models.CharField(blank=True, max_length=50, null=True, verbose_name='Pais del cliente')),
                ('biografy', models.TextField(blank=True, max_length=500, verbose_name='Biografia del perfil')),
                ('tasks_finalize', models.IntegerField(blank=True, default=0, verbose_name='Tareas finalizadas')),
                ('tasks_pending', models.IntegerField(blank=True, default=0, verbose_name='Tareas pendientes')),
                ('tasks_created', models.IntegerField(blank=True, default=0, verbose_name='Tareas creadas')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', 'modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
