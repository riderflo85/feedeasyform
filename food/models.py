from django.db import models


class Group(models.Model):
    name = models.CharField(
        max_length=45, verbose_name="Nom du groupe de l'aliment")
    
    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=45, verbose_name="Nom de l'aliment")
    description = models.TextField(verbose_name="Description")
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, verbose_name="Groupe de l'aliment")

    def __str__(self):
        return self.name