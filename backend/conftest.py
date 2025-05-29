import os
import django
from django.conf import settings
import pytest
from django.urls import reverse

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient() 