# Generated by Django 4.0.4 on 2022-05-26 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landConversion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='adhaar',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='phonenumber',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='pincode',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='thandaperu',
            field=models.BigIntegerField(),
        ),
    ]