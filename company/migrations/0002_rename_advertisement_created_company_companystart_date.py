# Generated by Django 5.0.4 on 2024-05-13 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='advertisement_created',
            new_name='CompanyStart_date',
        ),
    ]
