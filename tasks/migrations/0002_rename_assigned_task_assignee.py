# Generated by Django 4.1.5 on 2023-01-23 23:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task",
            old_name="assigned",
            new_name="assignee",
        ),
    ]
