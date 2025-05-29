import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
def test_successful_pdf_upload(client):
    # Create a test PDF file
    pdf_content = b"%PDF-1.4\n%Test PDF content"
    pdf_file = SimpleUploadedFile("test.pdf", pdf_content, content_type="application/pdf")

    # Make the upload request
    url = reverse("upload_file")
    response = client.post(url, {"file": pdf_file})

    # Check response
    assert response.status_code == 201
    data = response.json()
    assert "message" in data
    assert data["message"] == "File uploaded successfully"


@pytest.mark.django_db
def test_invalid_file_upload(client):
    # Create a test text file
    text_content = b"This is not a PDF file"
    text_file = SimpleUploadedFile("test.txt", text_content, content_type="text/plain")

    # Make the upload request
    url = reverse("upload_file")
    response = client.post(url, {"file": text_file})

    # Check response
    assert response.status_code == 400
    assert "file" in response.json()


def test_upload_pdf(api_client):
    # Create a test PDF file
    pdf_content = b"%PDF-1.4\n%Test PDF content"
    pdf_file = SimpleUploadedFile("test.pdf", pdf_content, content_type="application/pdf")

    # Make the upload request
    url = reverse("upload_file")
    response = api_client.post(url, {"file": pdf_file}, format="multipart")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {"message": "File uploaded successfully"}


def test_upload_invalid_file(api_client):
    # Create a test text file
    text_content = b"This is not a PDF file"
    text_file = SimpleUploadedFile("test.txt", text_content, content_type="text/plain")

    # Make the upload request
    url = reverse("upload_file")
    response = api_client.post(url, {"file": text_file}, format="multipart")
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Only PDF files are allowed" in response.json()["file"][0]
