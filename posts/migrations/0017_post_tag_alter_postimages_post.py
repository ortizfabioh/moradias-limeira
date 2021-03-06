# Generated by Django 4.0.2 on 2022-03-12 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_remove_tag_posts_remove_tag_slug'),
        ('posts', '0016_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
        migrations.AlterField(
            model_name='postimages',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.post'),
            preserve_default=False,
        ),
    ]
