# Generated by Django 2.2.6 on 2020-02-11 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inbox',
            name='is_html_content',
        ),
        migrations.AddField(
            model_name='inbox',
            name='raw_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
