# Generated by Django 4.0.3 on 2022-04-03 23:06

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0002_cerrajero_folleto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cerrajero',
            name='folleto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
