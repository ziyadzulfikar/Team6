# Generated by Django 4.0.4 on 2022-05-27 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landConversion', '0007_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thandaperu', models.BigIntegerField()),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField()),
                ('pincode', models.BigIntegerField()),
                ('phonenumber', models.BigIntegerField()),
                ('adhaar', models.BigIntegerField()),
                ('landSize', models.BigIntegerField()),
                ('landBefore', models.CharField(max_length=100)),
                ('landAfter', models.CharField(max_length=100)),
                ('thalukVerification', models.CharField(max_length=100)),
                ('villageVerification', models.CharField(max_length=100)),
                ('notification', models.BooleanField(default=False)),
            ],
        ),
    ]
