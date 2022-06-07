# Generated by Django 4.0.5 on 2022-06-06 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0010_movie_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='currency',
            field=models.CharField(choices=[('E', '€'), ('D', '$'), ('R', '₽')], default='R', max_length=1),
        ),
    ]