# Generated by Django 4.0.4 on 2022-05-24 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='imagem',
        ),
    ]
