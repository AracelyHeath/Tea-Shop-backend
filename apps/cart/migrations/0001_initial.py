# Generated by Django 5.0.4 on 2024-04-25 03:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0002_alter_item_updated_at'),
        ('user', '0002_alter_user_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created_at')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
    ]
