# Generated by Django 4.1 on 2022-08-21 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("userpanel", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profiledocumentmodel",
            name="custom_documents",
        ),
    ]
