# Generated by Django 2.2.1 on 2019-06-18 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='protection',
            field=models.BooleanField(default=False),
        ),
    ]
