# Generated by Django 4.1.7 on 2023-03-29 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0008_user_isadmin_alter_bookmanageruser_admincreator_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="ISADMIN",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="is_manager",
            field=models.BooleanField(default=True),
        ),
    ]