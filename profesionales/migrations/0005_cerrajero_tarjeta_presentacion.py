# Generated by Django 4.0.3 on 2022-04-10 15:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0004_remove_cerrajero_folleto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerrajero',
            name='tarjeta_presentacion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
