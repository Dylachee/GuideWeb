# Generated by Django 4.2.1 on 2023-05-26 10:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0002_initial'),
        ('objects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='favorite',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='order',
            name='clothes',
        ),
        migrations.AddField(
            model_name='cart',
            name='clothing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.traditionalclothing'),
        ),
        migrations.AddField(
            model_name='order',
            name='clothing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='clothes.traditionalclothing'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='food',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.traditionalfood'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='food',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='objects.traditionalfood'),
        ),
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
