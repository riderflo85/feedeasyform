from django.db import models

from food.models import Food, Allergie


class Season(models.Model):
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="saison de l'année"
    )

    def __str__(self):
        return self.name


class DietaryPlan(models.Model):
    name = models.CharField(
        max_length=45,
        unique=True,
        verbose_name="régime alimentaire"
    )
    description = models.TextField(
        verbose_name="courte description"
    )

    def __str__(self):
        return self.name


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
    image_active = models.ImageField(
        upload_to="recipe/pictures",
        blank=True,
        null=True,
        verbose_name="image active de la categorie"
    )
    image_not_active = models.ImageField(
        upload_to="recipe/pictures",
        blank=True,
        null=True,
        verbose_name="image non active de la categorie"
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
    tip = models.TextField(
        verbose_name="astuces divers"
    )
    portion = models.IntegerField(
        verbose_name="nombre de portions pour la recette",
        default=1
    )
    point = models.IntegerField(
        verbose_name="point de la recette",
        default=1
    )
    typical_recipe_city = models.CharField(
        max_length=255,
        null=True,
        verbose_name="recette typique de la ville de"
    )
    source = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name="source de la recette"
    )
    image = models.ImageField(
        upload_to="recipe/pictures",
        blank=True,
        null=True,
        verbose_name="image de la recette"
    )
    food = models.ManyToManyField(
        Food,
        through="FoodAndQuantity",
        verbose_name="ingredients avec quantitees"
    )
    categories = models.ManyToManyField(
        CategorieRecipe,
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
    season = models.ManyToManyField(
        Season,
        verbose_name="saison de la recette"
    )
    dietary_plan = models.ManyToManyField(
        DietaryPlan,
        verbose_name="régime alimentaire de la recette"
    )
    allergies = models.ManyToManyField(
        Allergie,
        verbose_name="allergies possible dans la recette"
    )

    def __str__(self):
        return self.name

    def get_step(self):
        steps = self.step.split('\n')
        return steps

    def get_tip(self):
        tips = self.tip.split('\n')
        return tips

    def get_all_foods(self):
        foods = []

        for food in self.food.all():
            f = FoodAndQuantity.objects.get(food=food, recipe=self)
            foods.append(f)

        return foods

    def list_fields_without_verbose_name(self):
        """
        Return a iterator for get the all fields 
        without a verbose name and with values.
        """

        for field in self._meta.fields:
            yield (field.name, field.value_to_string(self))


class FoodAndQuantity(models.Model):
    UNITS = [
        ("Null", "Not defined"),
        # ("CUP", "Cup"),
        ("Cuillère à soupe", "Cuillère à soupe"),
        ("Cuillère à café", "Cuillère à café"),
        ("Cl", "Centilitre"),
        ("Gr", "Gramme"),
        ("Unité", "Unité"),
        ("Pincée", "Pincée"),
        # ("FL OZ", "Fluid Ounce"),
        # ("OZ", "Ounce"),
    ]

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
    recipe_quantity = models.CharField(
        max_length=100,
        verbose_name="quantitée de l'ingredient pour la recette"
    )
    recipe_unity = models.CharField(
        max_length=20,
        choices=UNITS,
        verbose_name="unité de mesure de l'ingrédient pour la recette"
    )
    food_purchase_quantity = models.CharField(
        max_length=100,
        verbose_name="quantitée de l'ingredient pour la liste d'achats"
    )
    food_purchase_unity = models.CharField(
        max_length=35,
        choices=UNITS,
        default=UNITS[0][1],
        verbose_name="unité de mesure de l'ingrédient pour la liste d'achats"
    )

    def set_purchase_quantity(self):
        """
        Set the purchase quantity with a type of unity.
        """
        quant = float(self.recipe_quantity)
        unity = self.recipe_unity
        purchase_quant = 0.0

        if unity == "CaS":
            purchase_quant = quant * 1.5

        elif unity == "CaC":
            purchase_quant = quant * 0.5
        
        else:
            purchase_quant = quant
        
        self.food_purchase_quantity = str(purchase_quant)
        self.save()
