# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Roles
from .serializers import RolesSerializers


class RolesView(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RolesSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def __str__(self):
        return role_name
