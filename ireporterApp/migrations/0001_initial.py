# Generated by Django 3.2.8 on 2021-10-19 07:47

import cloudinary_storage.storage
import cloudinary_storage.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import ireporterApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RedFlag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=43)),
                ('description', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('received', 'received'), ('investigating', 'investigating'), ('rejected', 'rejected'), ('resolved', 'resolved')], default='received', max_length=20)),
                ('redFlag_image', models.ImageField(upload_to=ireporterApp.models.redflag_image_upload)),
                ('redFlag_video', models.FileField(blank=True, max_length=4000, null=True, storage=cloudinary_storage.storage.VideoMediaCloudinaryStorage(), upload_to=ireporterApp.models.redflag_video_upload, validators=[cloudinary_storage.validators.validate_video])),
                ('redFlag_location', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.TextField(max_length=200)),
                ('description', models.TextField(max_length=100)),
                ('status', models.CharField(choices=[('received', 'received'), ('investigating', 'investigating'), ('rejected', 'rejected'), ('resolved', 'resolved')], default='received', max_length=20)),
                ('location', models.TextField(max_length=90)),
                ('intervention_image', models.ImageField(upload_to=ireporterApp.models.redflag_image_upload)),
                ('video', models.CharField(blank=True, max_length=20, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervention_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
