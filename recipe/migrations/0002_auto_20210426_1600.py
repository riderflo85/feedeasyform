# Generated by Django 3.2 on 2021-04-26 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_allergie'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='allergies',
            field=models.ManyToManyField(to='food.Allergie', verbose_name='allergies possible dans la recette'),
        ),
        migrations.AlterField(
            model_name='foodandquantity',
            name='food_purchase_unity',
            field=models.CharField(choices=[('Null', 'Not defined'), ('CaS', 'Cuillère à soupe'), ('CaC', 'Cuillère à café'), ('CL', 'Centilitre'), ('GR', 'Gramme'), ('U', 'Unité'), ('Pincee', 'Pincée')], default='Not defined', max_length=35, verbose_name="unité de mesure de l'ingrédient pour la liste d'achats"),
        ),
        migrations.AlterField(
            model_name='foodandquantity',
            name='recipe_unity',
            field=models.CharField(choices=[('Null', 'Not defined'), ('CaS', 'Cuillère à soupe'), ('CaC', 'Cuillère à café'), ('CL', 'Centilitre'), ('GR', 'Gramme'), ('U', 'Unité'), ('Pincee', 'Pincée')], max_length=20, verbose_name="unité de mesure de l'ingrédient pour la recette"),
        ),
    ]