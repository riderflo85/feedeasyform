# Generated by Django 3.2.4 on 2021-08-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_auto_20210512_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealsperday',
            name='weight',
            field=models.IntegerField(default=0, verbose_name='poids du type de repas (pour définir un filtre)'),
        ),
    ]
