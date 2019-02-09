from rest_framework import serializers
from .models import Roles


class RolesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('id', 'role_class', 'role_name')
