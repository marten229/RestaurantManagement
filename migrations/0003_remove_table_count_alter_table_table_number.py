# Generated by Django 5.0.3 on 2024-06-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagement', '0002_remove_restaurant_address_restaurant_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='count',
        ),
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(),
        ),
    ]
