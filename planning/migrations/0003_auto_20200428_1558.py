# Generated by Django 3.0.5 on 2020-04-28 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20200428_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=45, verbose_name='Nom de la recette'),
        ),
    ]
