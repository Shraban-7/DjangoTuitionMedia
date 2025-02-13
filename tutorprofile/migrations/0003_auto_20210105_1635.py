# Generated by Django 3.1.4 on 2021-01-05 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorprofile', '0002_auto_20210105_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='tutorinfo',
            name='prefer_area_to_teach',
            field=models.CharField(max_length=600, null=True),
        ),
    ]
