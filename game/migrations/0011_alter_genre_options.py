# Generated by Django 4.2.7 on 2023-11-17 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0010_gamegenre_game_genres'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['name']},
        ),
    ]
