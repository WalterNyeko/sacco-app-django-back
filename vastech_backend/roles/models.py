# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Roles(models.Model):
    role_class = models.CharField(max_length=100)
    role_name = models.CharField(max_length=100)
