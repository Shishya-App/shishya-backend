# Generated by Django 4.1 on 2022-08-25 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0006_alter_user_key"),
    ]

    operations = [
        migrations.CreateModel(
            name="verifyOTP",
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
                ("otp", models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="key",
        ),
    ]