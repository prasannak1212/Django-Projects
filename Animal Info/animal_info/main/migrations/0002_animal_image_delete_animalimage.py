# Generated by Django 5.1.4 on 2025-01-01 18:06

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='animal_images/'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='AnimalImage',
        ),
    ]
