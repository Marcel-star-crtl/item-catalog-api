# Generated by Django 4.2.16 on 2024-09-07 17:59

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("items", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="stock",
            field=models.PositiveIntegerField(
                default=1, validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AddField(
            model_name="item",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=10,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
