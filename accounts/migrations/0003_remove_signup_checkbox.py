# Generated by Django 3.0.8 on 2020-07-14 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_signup_checkbox'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='checkbox',
        ),
    ]