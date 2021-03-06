# Generated by Django 3.0.8 on 2020-07-19 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20200718_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Eventform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('event_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('link', models.CharField(max_length=1000)),
                ('number', models.CharField(max_length=20)),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
            ],
        ),
    ]
