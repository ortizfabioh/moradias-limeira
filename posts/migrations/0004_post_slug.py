# Generated by Django 4.0.2 on 2022-02-19 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_regularpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='default-slug'),
            preserve_default=False,
        ),
    ]