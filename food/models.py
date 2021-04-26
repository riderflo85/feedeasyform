from django.db import models


class FoodGroup(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        verbose_name="nom du groupe d'ingredient"
    )

    def __str__(self):
        return self.name


class Food(models.Model):
    METRIC_UNITS = [
        ("CL", "Centilitre"),
        ("GR", "Gramme"),
    ]
    IMPERIAL_UNIT = [
        ("FL OZ", "Fluid Ounce"),
        ("OZ", "Ounce"),
    ]

    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name="nom de l'ingredient"
    )
    food_code = models.IntegerField(
        unique=True,
        null=True,
        verbose_name="code aliment"
    )
    id_group = models.ForeignKey(
        FoodGroup,
        on_delete=models.CASCADE,
        verbose_name="groupe de l'ingredient"
    )
    proteine = models.CharField(
        max_length=15,
        null=True,
        verbose_name="proteines (g/100g)"
    )
    glucide = models.CharField(
        max_length=15,
        null=True,
        verbose_name="glucides (g/100g)"
    )
    sucre = models.CharField(
        max_length=15,
        null=True,
        verbose_name="sucres (g/100g)"
    )
    fibre = models.CharField(
        max_length=15,
        null=True,
        verbose_name="fibres (g/100g)"
    )
    lipide = models.CharField(
        max_length=15,
        null=True,
        verbose_name="lipides (g/100g)"
    )
    acide_gras_sature = models.CharField(
        max_length=15,
        null=True,
        verbose_name="acides gras satures (g/100g)"
    )
    cholesterol = models.CharField(
        max_length=15,
        null=True,
        verbose_name="cholesterol (mg/100g)"
    )
    sel_chlorure_de_sodium = models.CharField(
        max_length=15,
        null=True,
        verbose_name="sel | chlorure de sodium (g/100g)"
    )
    potassium = models.CharField(
        max_length=15,
        null=True,
        verbose_name="potassium (mg/100g)"
    )
    calcium = models.CharField(
        max_length=15,
        null=True,
        verbose_name="calcium (mg/100g)"
    )
    magnesium = models.CharField(
        max_length=15,
        null=True,
        verbose_name="magnesium (mg/100g)"
    )
    fer = models.CharField(
        max_length=15,
        null=True,
        verbose_name="fer (mg/100g)"
    )
    zinc = models.CharField(
        max_length=15,
        null=True,
        verbose_name="zinc (mg/100g)"
    )
    vitamine_c = models.CharField(
        max_length=15,
        null=True,
        verbose_name="vitamine C (mg/100g)"
    )
    vitamine_d = models.CharField(
        max_length=15,
        null=True,
        verbose_name="vitamine D (µg/100g)"
    )
    vitamine_e = models.CharField(
        max_length=15,
        null=True,
        verbose_name="vitamine E (mg/100g)"
    )
    energie = models.CharField(
        max_length=15,
        null=True,
        verbose_name="energie (kcal/100g)"
    )
    metric_unit = models.CharField(
        max_length=25,
        choices=METRIC_UNITS,
        default="not defined",
        verbose_name="unité métrique de base"
    )
    imperial_unit = models.CharField(
        max_length=25,
        choices=IMPERIAL_UNIT,
        default="not defined",
        verbose_name="unité impériale de base"
    )

    def __str__(self):
        return self.name

    def list_fields(self):
        """
        Return a iterator for get the all fields and values.
        """

        for field in self._meta.fields:
            yield (field.verbose_name, field.value_to_string(self))

    def list_fields_without_verbose_name(self):
        """
        Return a iterator for get the all fields 
        without a verbose name and with values.
        """

        for field in self._meta.fields:
            yield (field.name, field.value_to_string(self))


class Allergie(models.Model):
    name = models.CharField(
        max_length=70,
        null=True,
        unique=True,
        verbose_name="allergie"
    )

    def __str__(self):
        return self.name
