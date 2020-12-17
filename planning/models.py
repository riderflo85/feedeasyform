from django.db import models

from food.models import Food

class Utensil(models.Model):
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="nom de l'ustensil de cuisine",
    )

    def __str__(self):
        return self.name


class CategorieRecipe(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="nom de la catégorie de recette"
    )

    def __str__(self):
        return self.name


class Level(models.Model):
    name = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="nom du niveau de la difficultée de la recette"
    )

    def __str__(self):
        return self.name


class PriceScale(models.Model):
    name = models.CharField(
        max_length=25,
        unique=True,
        verbose_name="nom de la fourchette de prix de la recette"
    )

    def __str__(self):
        return self.name


class OriginRecipe(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="origine de la recette (pays/culture...)"
    )

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(
        max_length=55,
        unique=True,
        verbose_name="nom de la recette"
    )
    preparation_time = models.CharField(
        max_length=10,
        verbose_name="temps de préparation"
    )
    cooking_time = models.CharField(
        max_length=10,
        verbose_name="temps de cuisson"
    )
    step = models.TextField(
        verbose_name="étapes de préparation de la recette"
    )
    portion = models.IntegerField(
        verbose_name="nombre de portions pour la recette",
        default=1
    )
    point = models.IntegerField(
        verbose_name="point de la recette",
        default=1
    )
    food = models.ManyToManyField(
        Food,
        through="FoodAndQuantity",
        verbose_name="ingredients avec quantitees"
    )
    categorie = models.ForeignKey(
        CategorieRecipe,
        on_delete=models.CASCADE,
        verbose_name="categorie de la recette"
    )
    origin = models.ForeignKey(
        OriginRecipe,
        on_delete=models.CASCADE,
        verbose_name="origine de la recette"
    )
    price_scale = models.ForeignKey(
        PriceScale,
        on_delete=models.CASCADE,
        verbose_name="frouchette de prix de la recette"
    )
    level = models.ForeignKey(
        Level,
        on_delete=models.CASCADE,
        verbose_name="niveau de difficulté de la recette"
    )
    utensils = models.ManyToManyField(
        Utensil,
        verbose_name="ustensils nécessaire pour la recette"
    )

    def __str__(self):
        return self.name

    def get_step(self):
        steps = self.step.split('\n')
        return steps

    def get_all_foods(self):
        foods = []

        for food in self.food.all():
            f = FoodAndQuantity.objects.get(food=food, recipe=self)
            foods.append(f)

        return foods


class FoodAndQuantity(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        verbose_name="recette"
    )
    food = models.ForeignKey(
        Food,
        on_delete=models.CASCADE,
        verbose_name="ingredient"
    )
    quantity = models.CharField(
        max_length=100,
        verbose_name="quantitee de l'ingredient avec l'unite de mesure"
    )


# from django.db import models
# from food.models import Food


# class FoodQuantity(models.Model):
#     quantity = models.CharField(max_length=45, verbose_name="Quantité de l'aliment")
#     food = models.ForeignKey(Food, on_delete=models.CASCADE, verbose_name="Aliment")

#     def __str__(self):
#         return f"{self.food}: {self.quantity}"


# class Categorie(models.Model):
#     name = models.CharField(max_length=45, verbose_name='Nom de la catégorie')

#     def __str__(self):
#         return self.name


# class Utensil(models.Model):
#     name = models.CharField(max_length=45, verbose_name="Nom de l'ustensile de cuisine")

#     def __str__(self):
#         return self.name


# PRICE_SCALE = [
#     ('low', 'petit budget'),
#     ('medium', 'moyen budget'),
#     ('high', 'gros budget')
# ]

# LEVEL = [
#     ('easy', 'facile'),
#     ('medium', 'moyen'),
#     ('chef', 'chef')
# ]

# class Recipe(models.Model):
#     name = models.CharField(max_length=45, verbose_name='Nom de la recette')

#     prepare_duration = models.CharField(
#         max_length=45, verbose_name='Temps de préparation')

#     cooking_time = models.CharField(
#         max_length=45, verbose_name='Temps de cuisson')

#     step = models.TextField(verbose_name='Étapes de la recette')

#     food_quantity = models.ManyToManyField(
#         FoodQuantity, verbose_name='Aliment et quantité')

#     categorie = models.ForeignKey(
#         Categorie,
#         on_delete=models.CASCADE,
#         verbose_name='Nom de la categorie de la recette'
#     )

#     price_scale = models.CharField(
#         max_length=45, choices=PRICE_SCALE, verbose_name='Fouchette de prix')

#     level = models.CharField(
#         max_length=45, choices=LEVEL, verbose_name='Difficultée')
        
#     utensil = models.ManyToManyField(
#         Utensil, verbose_name='Ustensile de cuisine')

#     def __str__(self):
#         return self.name
    
#     def get_price_scale(self):
#         type_price = {
#             'low': 'Petit budget',
#             'medium': 'Moyen budget',
#             'high': 'Gros budget'
#         }
#         return type_price[self.price_scale]
    
#     def get_level(self):
#         level = {
#             'easy': 'Facile',
#             'medium': 'Moyen',
#             'chef': 'Chef'
#         }
#         return level[self.level]

#     def get_step(self):
#         steps = self.step.split('\n')
#         return steps