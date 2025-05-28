from rest_framework import serializers
import os

class PDFUploadSerializer(serializers.Serializer):
    file = serializers.FileField()

    def validate_file(self, value):
        # Check file extension
        ext = os.path.splitext(value.name)[1].lower()
        if ext != '.pdf':
            raise serializers.ValidationError('Only PDF files are allowed.')

        # Check content type
        content_type = value.content_type
        if content_type != 'application/pdf':
            raise serializers.ValidationError('File must be a PDF.')

        return value 