# Generated by Django 4.1.7 on 2023-03-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelsapp', '0002_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='img1',
            field=models.ImageField(upload_to='pics1'),
        ),
    ]