# Generated by Django 2.0.7 on 2018-09-01 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeoBookAPI', '0005_remove_usuario_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(blank=True, max_length=50)),
                ('contrasena', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
