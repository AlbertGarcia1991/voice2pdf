import pytest
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
import os
from django.conf import settings
from rest_framework import status


@pytest.mark.django_db
def test_successful_pdf_upload(client):
    # Create a test PDF file
    pdf_content = b'%PDF-1.4\n%Test PDF content'
    pdf_file = SimpleUploadedFile(
        "test.pdf",
        pdf_content,
        content_type="application/pdf"
    )

    # Make the upload request
    url = reverse('pdf_upload')
    response = client.post(url, {'file': pdf_file})

    # Check response
    assert response.status_code == 200
    data = response.json()
    assert 'upload_id' in data
    assert 'pages' in data
    assert data['pages'] == []

    # Check if file exists
    filepath = os.path.join(settings.PDF_TMP_DIR, f"{data['upload_id']}.pdf")
    assert os.path.exists(filepath)

    # Cleanup
    os.remove(filepath)


@pytest.mark.django_db
def test_invalid_file_upload(client):
    # Create a test text file
    text_content = b'This is not a PDF file'
    text_file = SimpleUploadedFile(
        "test.txt",
        text_content,
        content_type="text/plain"
    )

    # Make the upload request
    url = reverse('pdf_upload')
    response = client.post(url, {'file': text_file})

    # Check response
    assert response.status_code == 400
    assert 'file' in response.json()


def test_upload_pdf(api_client):
    url = reverse('upload_file')
    with open('test.pdf', 'rb') as f:
        response = api_client.post(url, {'file': f}, format='multipart')
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'message': 'File uploaded successfully'}


def test_upload_invalid_file(api_client):
    url = reverse('upload_file')
    with open('test.txt', 'rb') as f:
        response = api_client.post(url, {'file': f}, format='multipart')
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'Only PDF files are allowed' in response.json()['file'][0]
