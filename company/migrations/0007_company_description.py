# Generated by Django 5.0.4 on 2024-05-17 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_link_to_page_company_location_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
