from django.db import models

# Create your models here.
class BetaUser(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name="adresse email du beta testeur"
    )