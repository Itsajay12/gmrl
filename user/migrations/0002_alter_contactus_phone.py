# Generated by Django 5.0 on 2023-12-22 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.BigIntegerField(),
        ),
    ]