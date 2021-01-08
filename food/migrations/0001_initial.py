# Generated by Django 3.1.5 on 2021-01-08 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name="nom du groupe d'ingredient")),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name="nom de l'ingredient")),
                ('proteine', models.CharField(max_length=15, null=True, verbose_name='proteines (g/100g)')),
                ('glucide', models.CharField(max_length=15, null=True, verbose_name='glucides (g/100g)')),
                ('sucre', models.CharField(max_length=15, null=True, verbose_name='sucres (g/100g)')),
                ('fibre', models.CharField(max_length=15, null=True, verbose_name='fibres (g/100g)')),
                ('lipide', models.CharField(max_length=15, null=True, verbose_name='lipides (g/100g)')),
                ('acide_gras_sature', models.CharField(max_length=15, null=True, verbose_name='acides gras satures (g/100g)')),
                ('cholesterol', models.CharField(max_length=15, null=True, verbose_name='cholesterol (mg/100g)')),
                ('sel_chlorure_de_sodium', models.CharField(max_length=15, null=True, verbose_name='sel | chlorure de sodium (g/100g)')),
                ('potassium', models.CharField(max_length=15, null=True, verbose_name='potassium (mg/100g)')),
                ('calcium', models.CharField(max_length=15, null=True, verbose_name='calcium (mg/100g)')),
                ('magnesium', models.CharField(max_length=15, null=True, verbose_name='magnesium (mg/100g)')),
                ('fer', models.CharField(max_length=15, null=True, verbose_name='fer (mg/100g)')),
                ('zinc', models.CharField(max_length=15, null=True, verbose_name='zinc (mg/100g)')),
                ('vitamine_c', models.CharField(max_length=15, null=True, verbose_name='vitamine C (mg/100g)')),
                ('vitamine_d', models.CharField(max_length=15, null=True, verbose_name='vitamine D (µg/100g)')),
                ('vitamine_e', models.CharField(max_length=15, null=True, verbose_name='vitamine E (mg/100g)')),
                ('metric_unit', models.CharField(default='kg', max_length=25, verbose_name='unité métrique de base')),
                ('imperial_unit', models.CharField(default='lb', max_length=25, verbose_name='unité impériale de base')),
                ('id_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.foodgroup', verbose_name="groupe de l'ingredient")),
            ],
        ),
    ]
