# Generated by Django 5.0.3 on 2024-06-10 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('RestaurantManagement', '0003_remove_table_count_alter_table_table_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='table_number',
        ),
    ]
