# Generated by Django 4.1 on 2022-08-21 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("adminpanel", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="form",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="question",
                to="adminpanel.form",
                verbose_name="Form.id",
            ),
        ),
    ]
