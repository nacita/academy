# Generated by Django 2.2.10 on 2020-11-06 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offices', '0019_page_type_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=512)),
                ('image', models.ImageField(upload_to='images/banners')),
                ('show_web', models.BooleanField()),
                ('show_app', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='page',
            name='type_content',
            field=models.PositiveIntegerField(choices=[(1, 'Page'), (2, 'Post')], default=2),
        ),
    ]