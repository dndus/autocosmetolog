# Generated by Django 3.2.9 on 2021-11-28 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20211128_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abouttext',
            old_name='entrance_textru',
            new_name='entrantext_ru',
        ),
        migrations.RenameField(
            model_name='abouttext',
            old_name='entrance_textuz',
            new_name='entrantext_uz',
        ),
    ]
