# Generated by Django 3.1.4 on 2020-12-09 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20201209_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='publicado',
            field=models.BooleanField(default=True, verbose_name='Publicar'),
        ),
    ]
