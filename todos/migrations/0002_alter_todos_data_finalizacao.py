# Generated by Django 5.0.4 on 2024-05-10 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todos",
            name="data_finalizacao",
            field=models.DateTimeField(null=True),
        ),
    ]