# Generated by Django 5.0.4 on 2024-05-10 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0003_alter_todos_data_criacao"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todos",
            name="data_criacao",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
