# Generated by Django 4.2.6 on 2023-11-10 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_post', '0011_routes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='routes',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
