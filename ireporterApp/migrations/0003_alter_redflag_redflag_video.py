# Generated by Django 3.2.8 on 2021-10-13 14:33

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.db import migrations, models
import ireporterApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ireporterApp', '0002_alter_redflag_redflag_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redflag',
            name='redFlag_video',
            field=models.FileField(blank=True, max_length=4000, null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to=ireporterApp.models.redflag_video_upload, validators=[cloudinary_storage.validators.validate_video]),
        ),
    ]
