# Generated by Django 2.1.7 on 2019-06-29 06:39

import academy.apps.graduates.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('graduates', '0003_graduate_certificate_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduate',
            name='is_channeled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='student',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='students.Student'),
        ),
        migrations.AlterField(
            model_name='graduate',
            name='user',
            field=models.ForeignKey(on_delete=models.SET(academy.apps.graduates.models.get_sentinel_user), related_name='graduates', to=settings.AUTH_USER_MODEL),
        ),
    ]
