# Generated by Django 4.0.3 on 2022-04-17 20:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
