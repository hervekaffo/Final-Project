# Generated by Django 2.0.2 on 2018-02-10 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0011_auto_20180210_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='daily_rent',
            field=models.FloatField(),
        ),
    ]
