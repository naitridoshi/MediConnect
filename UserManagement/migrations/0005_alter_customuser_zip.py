# Generated by Django 4.2.1 on 2023-12-08 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("UserManagement", "0004_alter_customuser_zip"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser", name="zip", field=models.IntegerField(),
        ),
    ]
