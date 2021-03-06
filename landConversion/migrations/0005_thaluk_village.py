# Generated by Django 4.0.4 on 2022-05-27 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landConversion', '0004_delete_thaluk_delete_village'),
    ]

    operations = [
        migrations.CreateModel(
            name='thaluk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.BigIntegerField()),
                ('place', models.CharField(max_length=100)),
                ('pincode', models.BigIntegerField()),
                ('adhaar', models.BigIntegerField()),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='village',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phonenumber', models.BigIntegerField()),
                ('place', models.CharField(max_length=100)),
                ('pincode', models.BigIntegerField()),
                ('adhaar', models.BigIntegerField()),
                ('password', models.TextField()),
            ],
        ),
    ]
