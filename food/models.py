from django.db import models


class Group(models.Model):
    name = models.CharField(max_length=45)


class Food(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)  # new table

