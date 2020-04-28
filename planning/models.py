from django.db import models
from food.models import Food


class FoodQuantity(models.Model):
    quantity = models.CharField(max_length=45)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)


class Categorie(models.Model):
    name = models.CharField(max_length=45)


class Recipe(models.Model):
    name = models.CharField(max_length=45)
    prepare_duration = models.CharField(max_length=45)
    cooking_time = models.CharField(max_length=45)
    step = models.TextField()
    food_quantity = models.ManyToManyField(FoodQuantity)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price_scale = models.CharField(max_length=45)
    level = models.CharField(max_length=45)
