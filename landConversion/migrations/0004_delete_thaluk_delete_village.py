# Generated by Django 4.0.4 on 2022-05-27 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landConversion', '0003_thaluk_village'),
    ]

    operations = [
        migrations.DeleteModel(
            name='thaluk',
        ),
        migrations.DeleteModel(
            name='village',
        ),
    ]