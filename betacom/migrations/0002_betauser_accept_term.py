# Generated by Django 3.2 on 2021-06-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betacom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='betauser',
            name='accept_term',
            field=models.BooleanField(default=False, verbose_name='accepte de recevoir des e-mails'),
        ),
    ]
