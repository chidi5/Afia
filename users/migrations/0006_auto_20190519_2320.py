# Generated by Django 2.2.1 on 2019-05-19 22:20

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20190519_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
