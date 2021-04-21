# Generated by Django 3.2 on 2021-04-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0005_auto_20210415_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='imperial_unit',
            field=models.CharField(choices=[('FL OZ', 'Fluid Ounce'), ('OZ', 'Ounce')], default='not defined', max_length=25, verbose_name='unité impériale de base'),
        ),
        migrations.AlterField(
            model_name='food',
            name='metric_unit',
            field=models.CharField(choices=[('CL', 'Centilitre'), ('GR', 'Gramme')], default='not defined', max_length=25, verbose_name='unité métrique de base'),
        ),
    ]
