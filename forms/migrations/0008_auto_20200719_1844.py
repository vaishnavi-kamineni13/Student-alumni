# Generated by Django 3.0.8 on 2020-07-19 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_eventform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventform',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventform',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
