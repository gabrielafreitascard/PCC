# Generated by Django 4.0.4 on 2022-05-23 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='data_publicacao',
            field=models.DateField(auto_now_add=True),
        ),
    ]
