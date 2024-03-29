# Generated by Django 3.2.9 on 2021-11-18 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211116_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(upload_to='uploads/videos/')),
                ('title', models.CharField(blank=True, default=None, max_length=300, null=True)),
                ('like', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
