from apotek.app.models import Worker
from rest_framework import serializers

class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = '__all__'

    def validate_password(self, attrs):
        from django.contrib.auth.hashers import make_password
        return make_password(attrs)