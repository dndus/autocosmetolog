# Generated by Django 3.2.9 on 2021-11-18 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
    ]
