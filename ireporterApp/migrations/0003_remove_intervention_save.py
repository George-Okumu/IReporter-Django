# Generated by Django 3.2.8 on 2021-10-13 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ireporterApp', '0002_alter_redflag_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='intervention',
            name='save',
        ),
    ]
