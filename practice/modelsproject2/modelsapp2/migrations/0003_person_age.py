# Generated by Django 5.0.6 on 2024-05-24 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp2', '0002_rename_name_person_person_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]
