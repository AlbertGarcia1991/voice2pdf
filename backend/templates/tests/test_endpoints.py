import pytest
from rest_framework.test import APIClient
from templates.models import Template
from templates.serializers import TemplateSerializer


@pytest.mark.django_db
def test_template_create_and_retrieve():
    client = APIClient()
    payload = {
        "upload_id": "test-upload-789",
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
    # Save (POST)
    resp = client.post("/api/templates/", payload, format="json")
    assert resp.status_code == 201
    assert "template_id" in resp.data
    template_id = resp.data["template_id"]

    # DB assertions
    assert Template.objects.count() == 1
    template = Template.objects.get(id=template_id)
    assert template.upload_id == "test-upload-789"
    assert template.fields.count() == 2
    assert set(template.fields.values_list("field_id", flat=True)) == {"field1", "field2"}

    # Retrieve (GET)
    resp = client.get(f"/api/templates/{template_id}/")
    assert resp.status_code == 200
    expected = TemplateSerializer(template).data
    assert resp.json() == expected
