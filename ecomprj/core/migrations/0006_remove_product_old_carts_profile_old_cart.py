# Generated by Django 5.1.2 on 2024-12-06 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_old_cart_product_old_carts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='old_carts',
        ),
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
