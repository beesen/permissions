# Generated by Django 4.1.2 on 2022-11-03 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_project_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='created',
        ),
    ]