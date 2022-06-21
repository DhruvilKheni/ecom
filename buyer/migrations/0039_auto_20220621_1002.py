# Generated by Django 3.2.13 on 2022-06-21 10:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0038_auto_20220621_0920'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cid',
            field=models.CharField(default=uuid.UUID('40da23b7-25ac-471e-ad51-53f68cdfb6b7'), max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=uuid.UUID('5ea592d4-e509-4416-962e-4fd40a030bb4'), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=uuid.UUID('fb23043f-843a-431e-a837-a5514087ca9f'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
