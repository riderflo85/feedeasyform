from django.db import models
from food.models import Food


class FoodQuantity(models.Model):
    quantity = models.CharField(max_length=45)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.food}: {self.quantity}"


class Categorie(models.Model):
    name = models.CharField(max_length=45, verbose_name='Nom de la catégorie')

    def __str__(self):
        return self.name


PRICE_SCALE = [
    ('low', 'petit budget'),
    ('meduim', 'moyen budget'),
    ('high', 'gros budget')
]

LEVEL = [
    ('easy', 'facile'),
    ('meduim', 'moyen'),
    ('chef', 'chef')
]

class Recipe(models.Model):
    name = models.CharField(max_length=45, verbose_name='Nom de la recette')
    prepare_duration = models.CharField(
        max_length=45, verbose_name='Temps de préparation')
    cooking_time = models.CharField(
        max_length=45, verbose_name='Temps de cuisson')
    step = models.TextField(verbose_name='Étapes de la recette')
    food_quantity = models.ManyToManyField(
        FoodQuantity, verbose_name='Aliment et quantité')
    categorie = models.ForeignKey(
        Categorie, on_delete=models.CASCADE, verbose_name='Nom de la categorie de la recette')
    price_scale = models.CharField(
        max_length=45, choices=PRICE_SCALE, verbose_name='Fouchette de prix')
    level = models.CharField(max_length=45, choices=LEVEL, verbose_name='Difficultée')

    def __str__(self):
        return self.name
