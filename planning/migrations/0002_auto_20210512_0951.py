# Generated by Django 3.2 on 2021-05-12 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_auto_20210510_1520'),
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='dietary_plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.dietaryplan', verbose_name='régime alimentaire du planning'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planning',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.originrecipe', verbose_name='origine du planning'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='planning',
            name='premium',
            field=models.BooleanField(default=False, verbose_name='réservé aux membres abonnés'),
        ),
        migrations.AddField(
            model_name='planning',
            name='season',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='recipe.season', verbose_name='saison du planning'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='planning',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='nom du planning'),
        ),
    ]
