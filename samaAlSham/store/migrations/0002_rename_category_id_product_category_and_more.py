# Generated by Django 5.0.7 on 2024-11-10 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="category_id",
            new_name="category",
        ),
        migrations.RenameField(
            model_name="product_variation",
            old_name="product_id",
            new_name="product",
        ),
    ]
