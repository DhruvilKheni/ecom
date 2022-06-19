# Generated by Django 3.2.13 on 2022-06-19 12:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0029_auto_20220619_1223'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='cart',
            name='cid',
            field=models.CharField(default=uuid.UUID('dfe1f594-e43f-4eec-9b9d-1da500523b61'), max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=uuid.UUID('5be7d8de-2185-4c4a-b615-9132845a0087'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
