# Generated by Django 5.1.2 on 2025-01-26 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_rename_detailed_description_package_getaway_highlights_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='detailed_description',
            field=models.TextField(blank=True),
        ),
    ]
