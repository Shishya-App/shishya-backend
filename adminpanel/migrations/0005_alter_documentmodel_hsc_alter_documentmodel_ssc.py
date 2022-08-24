# Generated by Django 4.1 on 2022-08-24 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0004_alter_documentmodel_birthcertificate_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="documentmodel",
            name="HSC",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="adminpanel.hsc",
            ),
        ),
        migrations.AlterField(
            model_name="documentmodel",
            name="SSC",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="adminpanel.ssc",
            ),
        ),
    ]