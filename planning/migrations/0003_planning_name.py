# Generated by Django 3.1.5 on 2021-03-18 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planning', '0002_remove_day_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='planning',
            name='name',
            field=models.CharField(default='default', max_length=150, verbose_name='nom du planning'),
            preserve_default=False,
        ),
    ]
