# Generated by Django 5.0.6 on 2024-05-08 07:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_product_product_image2_product_product_image3"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="product_description",
            field=models.TextField(blank=True, null=True),
        ),
    ]
