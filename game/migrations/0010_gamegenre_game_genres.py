# Generated by Django 4.2.7 on 2023-11-17 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0009_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameGenre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='game.genre')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(through='game.GameGenre', to='game.genre'),
        ),
    ]
