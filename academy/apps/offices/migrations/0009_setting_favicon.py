# Generated by Django 2.2.10 on 2020-04-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0008_setting'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='favicon',
            field=models.ImageField(blank=True, null=True, upload_to='images/settings'),
        ),
    ]