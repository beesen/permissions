# Generated by Django 4.1.2 on 2022-11-03 08:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('respondents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_dt', models.DateField(default=None, null=True)),
                ('end_dt', models.DateField(default=None, null=True)),
                ('invited_dt', models.DateField(default=None, null=True)),
                ('received_dt', models.DateField(default=None, null=True)),
                ('measurement_dt', models.DateField(default=None, null=True)),
                ('n_invited', models.PositiveIntegerField(default=0)),
                ('respondent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='respondents.respondent')),
            ],
        ),
    ]
