# Generated by Django 2.2.1 on 2019-05-16 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='first_name',
        ),
    ]
