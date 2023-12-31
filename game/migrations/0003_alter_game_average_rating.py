# Generated by Django 4.2.7 on 2023-11-15 13:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_alter_game_developer_alter_game_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='average_rating',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.MaxValueValidator(10.0)]),
        ),
    ]
