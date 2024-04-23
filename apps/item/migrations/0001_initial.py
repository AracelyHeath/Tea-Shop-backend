# Generated by Django 5.0.4 on 2024-04-23 03:55

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Name')),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Price')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='Image')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
            ],
            options={
                'db_table': 'item',
            },
        ),
    ]
