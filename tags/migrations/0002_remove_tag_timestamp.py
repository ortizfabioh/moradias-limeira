# Generated by Django 4.0.2 on 2022-03-06 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='timestamp',
        ),
    ]