# Generated by Django 3.1.4 on 2021-01-05 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorinfo',
            name='phone_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
