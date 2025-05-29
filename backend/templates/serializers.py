from rest_framework import serializers

from .models import Field, Template


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = "__all__"
        read_only_fields = ("template",)


class TemplateSerializer(serializers.ModelSerializer):
    fields = FieldSerializer(many=True)

    class Meta:
        model = Template
        fields = ["id", "upload_id", "created_at", "fields"]
        read_only_fields = ("id", "created_at")

    def create(self, validated_data):
        fields_data = validated_data.pop("fields")
        template = Template.objects.create(**validated_data)
        for field_data in fields_data:
            field_data["template"] = template
            Field.objects.create(**field_data)
        return template

    def update(self, instance, validated_data):
        fields_data = validated_data.pop("fields", None)
        if fields_data is not None:
            # Delete existing fields
            instance.fields.all().delete()
            # Create new fields
            for field_data in fields_data:
                field_data["template"] = instance
                Field.objects.create(**field_data)

        # Update template fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
