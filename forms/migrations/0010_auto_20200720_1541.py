# Generated by Django 3.0.8 on 2020-07-20 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20200719_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventform',
            name='username',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='sellform',
            name='username',
            field=models.CharField(max_length=10),
        ),
    ]
