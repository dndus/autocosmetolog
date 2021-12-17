# Generated by Django 3.2.9 on 2021-11-16 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_carousel_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='page',
            field=models.CharField(blank=True, choices=[('INDEX', 'index'), ('SERVICE', 'service'), ('LOCATION', 'location'), ('ABOUT', 'about'), ('CAREER', 'career'), ('INFO', 'info')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]