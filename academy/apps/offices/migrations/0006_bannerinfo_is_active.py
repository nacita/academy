# Generated by Django 2.2.6 on 2020-01-21 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0005_bannerinfo_color_style'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerinfo',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
