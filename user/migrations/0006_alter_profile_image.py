# Generated by Django 5.0.4 on 2024-05-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0005_alter_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.URLField(blank=True, max_length=9999),
        ),
    ]
