# Generated by Django 4.0.3 on 2022-04-03 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerrajero',
            name='folleto',
            field=models.CharField(default='', max_length=500, null=True),
        ),
    ]
