# Generated by Django 3.0.7 on 2020-12-13 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OriginRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='origine de la recette (pays/culture...)')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='point',
            field=models.IntegerField(default=1, verbose_name='point de la recette'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='origin',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='planning.OriginRecipe', verbose_name='origine de la recette'),
            preserve_default=False,
        ),
    ]