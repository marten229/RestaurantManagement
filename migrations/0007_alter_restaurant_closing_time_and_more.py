# Generated by Django 5.0.3 on 2024-06-12 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagement', '0006_openingday_remove_restaurant_opening_hours_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='closing_time',
            field=models.TimeField(default='18:00'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='opening_time',
            field=models.TimeField(default='09:00'),
        ),
    ]