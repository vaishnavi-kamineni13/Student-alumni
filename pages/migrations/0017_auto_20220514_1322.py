# Generated by Django 3.2.9 on 2022-05-14 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_remove_books_favourite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('companyname', models.CharField(max_length=100)),
                ('usernameans', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Books',
        ),
        migrations.DeleteModel(
            name='Electronics',
        ),
        migrations.DeleteModel(
            name='Favourites',
        ),
        migrations.DeleteModel(
            name='Others',
        ),
        migrations.DeleteModel(
            name='Sports',
        ),
        migrations.DeleteModel(
            name='Stationery',
        ),
    ]
