# Generated by Django 3.0.5 on 2020-04-28 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='level',
            field=models.CharField(choices=[('easy', 'facile'), ('meduim', 'moyen'), ('chef', 'chef')], max_length=45),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='price_scale',
            field=models.CharField(choices=[('low', 'petit budget'), ('meduim', 'moyen budget'), ('high', 'gros budget')], max_length=45),
        ),
    ]
