# Generated by Django 2.0.7 on 2018-08-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeoBookAPI', '0002_auto_20180826_0315'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/img/'),
        ),
    ]