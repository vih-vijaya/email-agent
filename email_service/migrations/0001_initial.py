# Generated by Django 5.1.6 on 2025-04-01 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SenderRecipient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("sender_email", models.EmailField(max_length=254)),
                ("receiver_email", models.EmailField(max_length=254)),
            ],
        ),
    ]
