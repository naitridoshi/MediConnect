# Generated by Django 4.2.8 on 2023-12-12 16:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("UserManagement", "0015_alter_blogmodel_summary"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogmodel",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]