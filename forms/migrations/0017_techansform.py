# Generated by Django 3.2.9 on 2022-04-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0016_techform'),
    ]

    operations = [
        migrations.CreateModel(
            name='Techansform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('student_username', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=30)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.TextField()),
            ],
        ),
    ]
