# Generated by Django 4.0.2 on 2022-02-26 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=120),
        ),
    ]
