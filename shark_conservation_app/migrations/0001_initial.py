# Generated by Django 4.1 on 2022-08-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, verbose_name=' ')),
                ('location', models.TextField(blank=True, verbose_name=' ')),
                ('avg_length', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('diet', models.CharField(blank=True, default=' ', max_length=100)),
            ],
        ),
    ]
