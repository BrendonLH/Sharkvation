# Generated by Django 4.1 on 2022-08-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shark_conservation_app', '0002_shark_added_by_alter_shark_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shark',
            name='description',
        ),
        migrations.AddField(
            model_name='shark',
            name='info',
            field=models.TextField(default=' ', verbose_name=' '),
        ),
    ]