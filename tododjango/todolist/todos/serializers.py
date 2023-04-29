from rest_framework import serializers


class TodosSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    is_completed = serializers.BooleanField()