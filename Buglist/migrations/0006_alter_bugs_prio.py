# Generated by Django 4.1.5 on 2023-01-12 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buglist', '0005_remove_bugs_project_delete_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='prio',
            field=models.CharField(max_length=10),
        ),
    ]
