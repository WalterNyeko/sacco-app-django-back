# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class Profile(models.Model):

    username = models.CharField(max_length=255, primary_key=True)
    bio = models.TextField(null=True, blank=True)
    image = models.URLField(
        null=True,
        blank=True
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.username


def user_was_created(sender, instance, created, ** kwargs):
    """ Listen for when a user is creted and create a profile"""
    created and Profile.objects.create(
        user=instance, username=instance.username
    )


post_save.connect(user_was_created, sender=settings.AUTH_USER_MODEL)
