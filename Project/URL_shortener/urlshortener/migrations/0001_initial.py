# Generated by Django 4.1.7 on 2023-03-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.URLField(max_length=250)),
                ('shortened_part', models.CharField(blank=True, max_length=7, unique=True)),
                ('time_of_creation', models.DateTimeField(auto_now_add=True)),
                ('times_accessed', models.IntegerField(default=0)),
            ],
        ),
    ]
