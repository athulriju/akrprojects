# Generated by Django 4.1.5 on 2023-08-10 07:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("college", "0003_details"),
    ]

    operations = [
        migrations.AddField(
            model_name="details",
            name="gender",
            field=models.CharField(default=True, max_length=10),
        ),
    ]
