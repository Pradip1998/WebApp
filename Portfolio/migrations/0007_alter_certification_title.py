# Generated by Django 4.2.4 on 2023-08-21 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0006_certification_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certification',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
