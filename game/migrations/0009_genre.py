# Generated by Django 4.2.7 on 2023-11-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0008_platform_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('origin_date', models.DateField(null=True)),
            ],
        ),
    ]
