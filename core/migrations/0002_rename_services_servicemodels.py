# Generated by Django 5.0.6 on 2024-05-09 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='services',
            new_name='ServiceModels',
        ),
    ]