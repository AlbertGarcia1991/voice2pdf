from rest_framework import serializers
import os

class UploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        if not value.name.endswith('.pdf'):
            raise serializers.ValidationError('Only PDF files are allowed')
        return value 