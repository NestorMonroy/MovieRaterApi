# Generated by Django 3.1.2 on 2020-10-09 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='starts',
        ),
        migrations.AddField(
            model_name='rating',
            name='stars',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
            preserve_default=False,
        ),
    ]
