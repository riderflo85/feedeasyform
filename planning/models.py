from django.db import models
from recipe.models import Recipe, OriginRecipe, Season, DietaryPlan


class MealsPerDay(models.Model):
    name = models.CharField(
        max_length=15,
        null=True,
        verbose_name='nom du repas'
    )


class Day(models.Model):
    name = models.CharField(
        max_length=20,
        verbose_name='nom du jour de la semaine'
    )
    # date = models.DateField(
    #     verbose_name='date de ce jour'
    # )
    meals_per_day = models.ManyToManyField(
        MealsPerDay,
        through="DayMealsPerDay",
        verbose_name='type de repas dans la journée'
    )

    def __str__(self):
        return self.name


class DayMealsPerDay(models.Model):
    day = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name="jour de la semaine"
    )
    meal_per_day = models.ForeignKey(
        MealsPerDay,
        on_delete=models.CASCADE,
        verbose_name="type de repas"
    )
    recipes = models.ManyToManyField(
        Recipe,
        verbose_name="recettes présentent dans le repas",
    )


class Planning(models.Model):
    name = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="nom du planning"
    )
    premium = models.BooleanField(
        default=False,
        verbose_name="réservé aux membres abonnés"
    )
    season = models.ForeignKey(
        Season,
        on_delete=models.CASCADE,
        verbose_name="saison du planning"
    )
    origin = models.ForeignKey(
        OriginRecipe,
        on_delete=models.CASCADE,
        verbose_name="origine du planning"
    )
    dietary_plan = models.ForeignKey(
        DietaryPlan,
        on_delete=models.CASCADE,
        verbose_name="régime alimentaire du planning"
    )
    monday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='lundi',
        related_name='fk_monday'
    )
    tuesday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='mardi',
        related_name='fk_tuesday'
    )
    wednesday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='mercredi',
        related_name='fk_wednesday'
    )
    thursday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='jeudi',
        related_name='fk_thursday'
    )
    friday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='vendredi',
        related_name='fk_friday'
    )
    saturday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='samedi',
        related_name='fk_saturday'
    )
    sunday = models.ForeignKey(
        Day,
        on_delete=models.CASCADE,
        verbose_name='dimanche',
        related_name='fk_sunday'
    )