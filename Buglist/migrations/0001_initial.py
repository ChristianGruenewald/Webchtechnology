# Generated by Django 4.1.5 on 2023-01-09 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bugs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titel', models.CharField(max_length=30)),
                ('descripton', models.CharField(max_length=100)),
            ],
        ),
    ]
