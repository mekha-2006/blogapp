# Generated by Django 5.0.6 on 2024-06-07 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='Date',
            field=models.DateField(),
        ),
    ]
