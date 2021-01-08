# Generated by Django 3.1.5 on 2021-01-08 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategorieRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='nom de la catégorie de recette')),
            ],
        ),
        migrations.CreateModel(
            name='DietaryPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name='régime alimentaire')),
                ('description', models.TextField(verbose_name='courte description')),
            ],
        ),
        migrations.CreateModel(
            name='FoodAndQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.CharField(max_length=100, verbose_name="quantitee de l'ingredient avec l'unite de mesure")),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.food', verbose_name='ingredient')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, unique=True, verbose_name='nom du niveau de la difficultée de la recette')),
            ],
        ),
        migrations.CreateModel(
            name='OriginRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='origine de la recette (pays/culture...)')),
            ],
        ),
        migrations.CreateModel(
            name='PriceScale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='nom de la fourchette de prix de la recette')),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name="saison de l'année")),
            ],
        ),
        migrations.CreateModel(
            name='Utensil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True, verbose_name="nom de l'ustensil de cuisine")),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, unique=True, verbose_name='nom de la recette')),
                ('preparation_time', models.CharField(max_length=10, verbose_name='temps de préparation')),
                ('cooking_time', models.CharField(max_length=10, verbose_name='temps de cuisson')),
                ('step', models.TextField(verbose_name='étapes de préparation de la recette')),
                ('tip', models.TextField(verbose_name='astuces divers')),
                ('portion', models.IntegerField(default=1, verbose_name='nombre de portions pour la recette')),
                ('point', models.IntegerField(default=1, verbose_name='point de la recette')),
                ('typical_recipe_city', models.CharField(max_length=255, null=True, verbose_name='recette typique de la ville de')),
                ('source', models.CharField(blank=True, max_length=200, null=True, verbose_name='source de la recette')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe/picture/%Y/%m/%d', verbose_name='image de la recette')),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.categorierecipe', verbose_name='categorie de la recette')),
                ('dietary_plan', models.ManyToManyField(to='planning.DietaryPlan', verbose_name='régime alimentaire de la recette')),
                ('food', models.ManyToManyField(through='planning.FoodAndQuantity', to='food.Food', verbose_name='ingredients avec quantitees')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.level', verbose_name='niveau de difficulté de la recette')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.originrecipe', verbose_name='origine de la recette')),
                ('price_scale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.pricescale', verbose_name='frouchette de prix de la recette')),
                ('season', models.ManyToManyField(to='planning.Season', verbose_name='saison de la recette')),
                ('utensils', models.ManyToManyField(to='planning.Utensil', verbose_name='ustensils nécessaire pour la recette')),
            ],
        ),
        migrations.AddField(
            model_name='foodandquantity',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planning.recipe', verbose_name='recette'),
        ),
    ]
