# Generated by Django 4.1.7 on 2023-02-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buglist', '0006_alter_bugs_prio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='status',
            field=models.CharField(max_length=10),
        ),
    ]
