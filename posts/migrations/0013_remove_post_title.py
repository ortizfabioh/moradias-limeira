# Generated by Django 4.0.2 on 2022-03-06 02:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]
