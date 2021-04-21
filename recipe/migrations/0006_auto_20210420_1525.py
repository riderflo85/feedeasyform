# Generated by Django 3.2 on 2021-04-20 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_rename_categorie_recipe_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodandquantity',
            name='quantity',
        ),
        migrations.AddField(
            model_name='foodandquantity',
            name='food_purshase_quantity',
            field=models.CharField(default='null', max_length=100, verbose_name="quantitée de l'ingredient pour la liste d'achats"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foodandquantity',
            name='food_purshase_unity',
            field=models.CharField(choices=[('Null', 'Not defined'), ('CUP', 'Cup'), ('CaS', 'Cuillère à soupe'), ('CaC', 'Cuillère à café'), ('CL', 'Centilitre'), ('GR', 'Gramme'), ('FL OZ', 'Fluid Ounce'), ('OZ', 'Ounce')], default='Null', max_length=20, verbose_name="unité de mesure de l'ingrédient pour la liste d'achats"),
        ),
        migrations.AddField(
            model_name='foodandquantity',
            name='recipe_quantity',
            field=models.CharField(default='null', max_length=100, verbose_name="quantitée de l'ingredient pour la recette"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='foodandquantity',
            name='recipe_unity',
            field=models.CharField(choices=[('Null', 'Not defined'), ('CUP', 'Cup'), ('CaS', 'Cuillère à soupe'), ('CaC', 'Cuillère à café'), ('CL', 'Centilitre'), ('GR', 'Gramme'), ('FL OZ', 'Fluid Ounce'), ('OZ', 'Ounce')], max_length=20, verbose_name="unité de mesure de l'ingrédient pour la recette"),
        ),
    ]
