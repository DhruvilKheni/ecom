# Generated by Django 3.2.13 on 2022-06-19 12:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0031_auto_20220619_1227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ptype',
            new_name='type',
        ),
        migrations.AlterField(
            model_name='cart',
            name='cid',
            field=models.CharField(default=uuid.UUID('55a8fec9-dbf7-495d-b028-b33b7c336202'), max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=uuid.UUID('497f8688-0f1e-4eb0-a4a5-ee3e56a47666'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
