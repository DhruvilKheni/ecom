# Generated by Django 4.0 on 2022-06-17 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ipic',
            field=models.FileField(default='avatar.jpg', upload_to='product'),
        ),
    ]
