# Generated by Django 4.0.4 on 2022-05-16 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='jobid',
        ),
    ]
