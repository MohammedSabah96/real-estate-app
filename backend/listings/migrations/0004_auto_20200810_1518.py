# Generated by Django 3.1 on 2020-08-10 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_remove_listing_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='Listing',
            new_name='listing',
        ),
    ]
