# Generated by Django 3.2.8 on 2021-10-19 07:51

from django.db import migrations, models
import ireporterApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('ireporterApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervention',
            name='intervention_image',
            field=models.ImageField(upload_to=ireporterApp.models.intervention_image_upload),
        ),
    ]