# Generated by Django 4.0 on 2022-06-18 16:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0016_alter_cart_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='id',
        ),
        migrations.AddField(
            model_name='cart',
            name='cid',
            field=models.CharField(blank=True, default=uuid.UUID('a289fc16-5cf5-4a52-8a6c-8e758d060868'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
