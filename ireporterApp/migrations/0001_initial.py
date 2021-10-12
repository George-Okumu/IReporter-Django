# Generated by Django 3.2.8 on 2021-10-11 19:05

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
                ('status', models.CharField(blank=True, default='received', max_length=20, null=True)),
                ('redFlag_image', models.ImageField(blank=True, null=True, upload_to=ireporterApp.models.project_upload)),
                ('redFlag_video', models.CharField(blank=True, max_length=20, null=True)),
                ('redFlag_location', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='redflag', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
