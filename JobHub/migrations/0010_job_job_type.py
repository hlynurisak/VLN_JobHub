# Generated by Django 5.0.4 on 2024-05-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobHub', '0009_job_due_date_job_start_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_type',
            field=models.CharField(choices=[('FT', 'Full-time'), ('PT', 'Part-time')], default='FT', max_length=2),
        ),
    ]
