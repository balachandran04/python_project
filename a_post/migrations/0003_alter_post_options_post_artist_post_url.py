# Generated by Django 4.2.6 on 2023-10-17 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_post', '0002_post_body_post_image_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='post',
            name='artist',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='url',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
