# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import When, Case, Count, IntegerField
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import int_to_base36
from django.template.loader import render_to_string

from academy.core.utils import image_upload_path
from academy.core.validators import validate_mobile_phone
from academy.apps.students.models import Student, TrainingStatus

from model_utils import Choices
from post_office import mail


class CustomUserManager(UserManager):
    def create_user(self, username, email, password, is_active=False, **extra_fields):
        user = super().create_user(username, email, password, is_active=False, **extra_fields)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True, default=None,
                             validators=[validate_mobile_phone])
    ROLE = Choices(
        (1, 'student', 'Student'),
        (2, 'trainer', 'Trainer'),
        (2, 'company', 'Company'),
    )
    role = models.PositiveIntegerField(choices=ROLE, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = CustomUserManager()

    @property
    def name(self):
        name = self.get_full_name()
        if not name:
            name = self.username
        return name

    def get_student(self):
        return self.students.exclude(status=Student.STATUS.graduate).last()

    def notification_register(self):
        data = {
            'token': default_token_generator.make_token(self),
            'uid': int_to_base36(self.id),
            'host': settings.HOST,
            'user': self,
            'email_title': 'Aktivasi Akun'
        }

        send = mail.send(
            [self.email],
            settings.DEFAULT_FROM_EMAIL,
            subject='Aktivasi Akun',
            html_message=render_to_string('emails/register.html', context=data)
        )
        return send

    def notification_status_training(self, training_materials):
        data = {
            'host': settings.HOST,
            'user': self,
            'training_materials': training_materials,
            'email_title': 'Status Pelatihan'
        }

        send = mail.send(
            [self.email],
            settings.DEFAULT_FROM_EMAIL,
            subject='Status Pelatihan',
            html_message=render_to_string('emails/training-status.html', context=data)
        )
        return send
    
    def get_count_training_status(self):
        count_status = self.training_status.aggregate(
            graduate=Count(
                Case(When(status=TrainingStatus.STATUS.graduate, then=1),
                        output_field=IntegerField())
            ),
            not_yet=Count(
                Case(When(status=TrainingStatus.STATUS.not_yet, then=1),
                        output_field=IntegerField())
            ),
            repeat=Count(
                Case(When(status=TrainingStatus.STATUS.repeat, then=1),
                        output_field=IntegerField())
            )
        )
        return count_status


class Profile(models.Model):
    user = models.OneToOneField('accounts.User', related_name='profile')
    address = models.TextField()
    GENDER = Choices(
        (1, 'male', 'Male'),
        (2, 'female', 'Female'),
    )
    gender = models.PositiveIntegerField(choices=GENDER, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    organization_name = models.CharField(max_length=200, blank=True, null=True)
    avatar = models.ImageField(upload_to=image_upload_path('avatar'), blank=True, null=True)

    # Social fields
    linkedin = models.URLField(blank=True, max_length=255)
    git_repo = models.URLField(blank=True, max_length=255)
    blog = models.URLField(blank=True, max_length=255)
    facebook = models.URLField(blank=True, max_length=255)
    youtube = models.URLField(blank=True, max_length=255)
    twitter = models.CharField(blank=True, max_length=30)
    instagram = models.CharField(blank=True, max_length=30)
    telegram_id = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.username
