# Generated by Django 5.0.4 on 2024-05-17 22:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0004_alter_experience_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='application',
            name='recommendation',
        ),
        migrations.AddField(
            model_name='experience',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='application.application'),
        ),
        migrations.AddField(
            model_name='recommendation',
            name='application',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='recommendations', to='application.application'),
        ),
    ]
