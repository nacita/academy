# Generated by Django 2.2.6 on 2020-02-12 10:09

import ckeditor.fields
import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('offices', '0006_bannerinfo_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220, verbose_name='Judul')),
                ('slug', models.SlugField(blank=True, help_text='Generate otomatis jika dikosongkan', max_length=200)),
                ('short_content', ckeditor.fields.RichTextField(verbose_name='Konten Singkat')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Konten')),
                ('image', models.FileField(blank=True, upload_to='images/', verbose_name='Gambar')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Terlihat')),
                ('status', models.PositiveIntegerField(choices=[(1, 'Konsep'), (2, 'Terbit')], default=2)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to=settings.AUTH_USER_MODEL)),
                ('category', taggit.managers.TaggableManager(help_text='Kategori dipisahkan dengan koma', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Kategori')),
            ],
        ),
    ]
