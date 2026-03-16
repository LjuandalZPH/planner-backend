from rest_framework import serializers


class HealthSerializer(serializers.Serializer):
    message = serializers.CharField()

