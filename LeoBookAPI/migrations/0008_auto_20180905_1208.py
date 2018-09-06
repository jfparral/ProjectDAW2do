# Generated by Django 2.0.1 on 2018-09-05 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeoBookAPI', '0007_reportes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='descripcion_venta',
            name='id_libro',
        ),
        migrations.RemoveField(
            model_name='registro_ventas',
            name='id_descripcion_venta',
        ),
        migrations.RemoveField(
            model_name='registro_ventas',
            name='id_usuario',
        ),
        migrations.AddField(
            model_name='descripcion_venta',
            name='libro',
            field=models.CharField(default='Harry Potter', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro_ventas',
            name='cantidad',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro_ventas',
            name='libro',
            field=models.CharField(default='Harry Potter', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registro_ventas',
            name='usuario',
            field=models.CharField(default='leandre96', max_length=100),
            preserve_default=False,
        ),
    ]