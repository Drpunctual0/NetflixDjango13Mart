# Generated by Django 4.1.5 on 2023-06-05 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videolar/'),
        ),
    ]