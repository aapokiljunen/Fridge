# Generated by Django 4.2.1 on 2023-05-30 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fridge', '0002_manufacturer_created_manufacturer_modified_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thing',
            old_name='expirition_date',
            new_name='expiration_date',
        ),
    ]
