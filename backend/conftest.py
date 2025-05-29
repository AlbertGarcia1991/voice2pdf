import os
import django
import pytest


# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
