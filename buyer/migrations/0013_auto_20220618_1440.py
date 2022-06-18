# Generated by Django 3.2.13 on 2022-06-18 14:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0012_alter_cart_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.CharField(blank=True, default=uuid.UUID('2fa2fcd4-d97e-4da1-b634-3cb22e1a2eb5'), max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]
