# Generated by Django 3.0.8 on 2020-07-17 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200717_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='img',
            field=models.ImageField(upload_to='pics/'),
        ),
    ]
