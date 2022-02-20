# Generated by Django 4.0.2 on 2022-02-19 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_alter_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-datePost',)},
        ),
        migrations.RemoveField(
            model_name='post',
            name='regularPost',
        ),
        migrations.AddField(
            model_name='post',
            name='repuPost',
            field=models.BooleanField(default=False),
        ),
    ]
