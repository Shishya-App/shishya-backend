# Generated by Django 4.1 on 2022-08-25 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_alter_user_first_name_alter_user_last_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="adhaar_no",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="user",
            name="phone_no",
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]
