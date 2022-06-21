# Generated by Django 3.2.13 on 2022-06-21 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('buyer', '0039_auto_20220621_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(default='White', max_length=25),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.CharField(default='M', max_length=25),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cid',
            field=models.CharField(default=uuid.UUID('54244cd0-f5f2-4648-9396-f01be5bce749'), max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.CharField(default=uuid.UUID('dceee007-44db-47d6-9ef3-18e4246c5b55'), max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.CharField(default=uuid.UUID('927e5949-e439-4957-89b2-8f5503fb7cd8'), max_length=100, primary_key=True, serialize=False),
        ),
    ]
