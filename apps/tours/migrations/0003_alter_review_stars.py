# Generated by Django 4.2.1 on 2023-05-27 12:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_category_like_review_delete_raiting_tour_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]