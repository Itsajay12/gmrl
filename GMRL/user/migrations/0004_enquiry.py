# Generated by Django 5.0 on 2023-12-22 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_bookappontment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.BigIntegerField()),
                ('message', models.TextField()),
                ('received_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'Enquiry',
            },
        ),
    ]
