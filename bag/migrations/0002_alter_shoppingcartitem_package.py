# Generated by Django 5.1.2 on 2024-10-28 15:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bag', '0001_initial'),
        ('home', '0002_remove_package_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.package'),
        ),
    ]
