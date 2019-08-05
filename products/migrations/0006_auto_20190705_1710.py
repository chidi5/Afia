# Generated by Django 2.2.1 on 2019-07-05 16:10

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20190608_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fee',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(7000)]),
        ),
        migrations.AlterField(
            model_name='product',
            name='total',
            field=models.IntegerField(),
        ),
    ]