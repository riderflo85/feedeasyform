from django.db import models

# Create your models here.
class BetaUser(models.Model):
    email = models.EmailField(
        unique=True,
        verbose_name="adresse email du beta testeur"
    )
    accept_term = models.BooleanField(
        default=False,
        verbose_name="accepte de recevoir des e-mails"
    )