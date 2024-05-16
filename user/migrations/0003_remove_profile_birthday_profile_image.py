# Generated by Django 5.0.4 on 2024-05-16 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_profile_about_remove_profile_image_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="birthday",
        ),
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="",
                height_field=100,
                max_length=1000,
                upload_to="profile_pics",
                width_field=100,
            ),
        ),
    ]
