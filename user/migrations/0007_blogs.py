# Generated by Django 5.0 on 2023-12-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_packages_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='blogs')),
                ('date', models.DateField(auto_now=True)),
                ('desc', models.TextField()),
                ('sub1', models.CharField(blank=True, max_length=150)),
                ('desc1', models.TextField(blank=True)),
                ('sub2', models.CharField(blank=True, max_length=150)),
                ('desc2', models.TextField(blank=True)),
                ('sub3', models.CharField(blank=True, max_length=150)),
                ('desc3', models.TextField(blank=True)),
                ('sub4', models.CharField(blank=True, max_length=150)),
                ('desc4', models.TextField(blank=True)),
                ('sub5', models.CharField(blank=True, max_length=150)),
                ('desc5', models.TextField(blank=True)),
                ('sub6', models.CharField(blank=True, max_length=150)),
                ('desc6', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'Blogs',
            },
        ),
    ]