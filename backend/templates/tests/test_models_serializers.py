import pytest
from templates.models import Field, Template
from templates.serializers import TemplateSerializer


@pytest.mark.django_db
class TestTemplateModels:
    def test_create_template_with_fields(self):
        # Create a template
        template = Template.objects.create(upload_id="test-upload-123")

        # Create fields
        Field.objects.create(
            template=template,
            field_id="field1",
            type="text",
            label="Name",
            placeholder="Enter your name",
            page_number=1,
            x=100.0,
            y=200.0,
            width=300.0,
            height=50.0,
            validation={"required": True},
            value="John Doe",
        )
        Field.objects.create(
            template=template,
            field_id="field2",
            type="number",
            label="Age",
            placeholder="Enter your age",
            page_number=1,
            x=100.0,
            y=300.0,
            width=150.0,
            height=50.0,
            validation={"min": 0, "max": 120},
            value="25",
        )

        # Now assert
        assert template.fields.count() == 2


@pytest.mark.django_db
class TestTemplateSerializers:
    def test_template_serialization(self):
        # Create a template with fields
        template = Template.objects.create(upload_id="test-upload-123")

        # Create fields
        Field.objects.create(
            template=template,
            field_id="field1",
            type="text",
            label="Name",
            placeholder="Enter your name",
            page_number=1,
            x=100.0,
            y=200.0,
            width=300.0,
            height=50.0,
            validation={"required": True},
            value="John Doe",
        )
        Field.objects.create(
            template=template,
            field_id="field2",
            type="number",
            label="Age",
            placeholder="Enter your age",
            page_number=1,
            x=100.0,
            y=300.0,
            width=150.0,
            height=50.0,
            validation={"min": 0, "max": 120},
            value="25",
        )

        # Serialize the template
        serializer = TemplateSerializer(template)
        data = serializer.data

        # Assert serialized data structure
        assert "id" in data
        assert data["upload_id"] == "test-upload-123"
        assert "created_at" in data
        assert len(data["fields"]) == 2

        # Assert field data
        field1_data = next(f for f in data["fields"] if f["field_id"] == "field1")
        assert field1_data["type"] == "text"
        assert field1_data["label"] == "Name"
        assert field1_data["validation"] == {"required": True}
        assert field1_data["value"] == "John Doe"

        field2_data = next(f for f in data["fields"] if f["field_id"] == "field2")
        assert field2_data["type"] == "number"
        assert field2_data["label"] == "Age"
        assert field2_data["validation"] == {"min": 0, "max": 120}
        assert field2_data["value"] == "25"

    def test_template_deserialization(self):
        # Create test data
        template_data = {
            "upload_id": "test-upload-456",
            "fields": [
                {
                    "field_id": "field1",
                    "type": "text",
                    "label": "Name",
                    "placeholder": "Enter your name",
                    "page_number": 1,
                    "x": 100.0,
                    "y": 200.0,
                    "width": 300.0,
                    "height": 50.0,
                    "validation": {"required": True},
                    "value": "John Doe",
                },
                {
                    "field_id": "field2",
                    "type": "number",
                    "label": "Age",
                    "placeholder": "Enter your age",
                    "page_number": 1,
                    "x": 100.0,
                    "y": 300.0,
                    "width": 150.0,
                    "height": 50.0,
                    "validation": {"min": 0, "max": 120},
                    "value": "25",
                },
            ],
        }

        # Deserialize and save
        serializer = TemplateSerializer(data=template_data)
        assert serializer.is_valid()
        template = serializer.save()

        # Assert template was created correctly
        assert template.upload_id == "test-upload-456"
        assert template.fields.count() == 2

        # Assert fields were created correctly
        field1 = template.fields.get(field_id="field1")
        assert field1.type == "text"
        assert field1.label == "Name"
        assert field1.validation == {"required": True}
        assert field1.value == "John Doe"

        field2 = template.fields.get(field_id="field2")
        assert field2.type == "number"
        assert field2.label == "Age"
        assert field2.validation == {"min": 0, "max": 120}
        assert field2.value == "25"
