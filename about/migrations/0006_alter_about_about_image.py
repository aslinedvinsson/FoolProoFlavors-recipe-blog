# Generated by Django 4.2.9 on 2024-02-15 15:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_rename_profile_image_about_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_image',
            field=cloudinary.models.CloudinaryField(default='USE_STATIC_FALLBACK', max_length=255, verbose_name='image'),
        ),
    ]
