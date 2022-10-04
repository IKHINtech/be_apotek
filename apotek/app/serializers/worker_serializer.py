from apotek.app.models import Role, Worker
from rest_framework import serializers

from apotek.app.serializers.role_serializer import RoleSerializer


class WorkerSerializer(serializers.ModelSerializer):
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all(), many=True, write_only=True, source='roles')
    roles = RoleSerializer(many=True, read_only=True)

    class Meta:
        model = Worker
        fields = ['last_login', 'is_superuser', 'username', 'first_name', 'last_name',
                  'email', 'is_staff', 'is_active', 'date_joined', 'id', 'address', 'phone', 'role', 'roles']

    def validate_password(self, attrs):
        from django.contrib.auth.hashers import make_password
        return make_password(attrs)

    def create(self, validated_data):
        data = validated_data
        return super().create(validated_data)
