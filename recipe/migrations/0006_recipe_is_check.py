# Generated by Django 3.2 on 2021-06-27 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_auto_20210521_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_check',
            field=models.BooleanField(default=False, verbose_name='recette vérifiée ?'),
        ),
    ]