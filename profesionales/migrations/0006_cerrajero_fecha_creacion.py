# Generated by Django 4.0.3 on 2022-04-10 15:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0005_cerrajero_tarjeta_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cerrajero',
            name='fecha_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
