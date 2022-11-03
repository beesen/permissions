# Generated by Django 4.1.2 on 2022-11-03 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('surveys', '0001_initial'),
        ('moments', '0001_initial'),
        ('projects', '0002_project_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moment', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='moments.moment')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='projects.project')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='surveys.survey')),
            ],
        ),
    ]
