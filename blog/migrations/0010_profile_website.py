# Generated by Django 4.0.3 on 2022-05-29 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_profile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='website',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
