# Generated by Django 4.2.1 on 2023-05-30 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0005_alter_thing_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thing',
            options={'ordering': ['expiration_date']},
        ),
    ]
