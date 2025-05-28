# API Documentation

This document provides detailed information about the Voice2PDF API endpoints.

## Base URL

All API endpoints are relative to the base URL:
```
http://localhost:8000/api/
```

## Authentication

Currently, the API does not require authentication. This will be implemented in future versions.

## Endpoints

### Health Check

Check if the API is running properly.

```http
GET /api/health/
```

#### Response

```json
{
    "status": "ok"
}
```

### PDF Upload

Upload a PDF file for processing.

```http
POST /api/upload/
```

#### Request

- Method: `POST`
- Content-Type: `multipart/form-data`
- Body:
  - `file`: PDF file (required)

#### Example using curl

```bash
curl -X POST -F "file=@test.pdf" http://localhost:8000/api/upload/
```

#### Example using Python

```python
import requests

url = "http://localhost:8000/api/upload/"
files = {"file": open("test.pdf", "rb")}
response = requests.post(url, files=files)
print(response.json())
```

#### Example using JavaScript

```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('http://localhost:8000/api/upload/', {
  method: 'POST',
  body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

#### Response

Success (200 OK):
```json
{
    "upload_id": "123e4567-e89b-12d3-a456-426614174000",
    "pages": []
}
```

Error (400 Bad Request):
```json
{
    "error": "Only PDF files are allowed"
}
```

## Error Handling

The API uses standard HTTP status codes:

- 200: Success
- 400: Bad Request (invalid input)
- 404: Not Found
- 500: Internal Server Error

### Error Response Format

```json
{
    "error": "Error message description"
}
```

## Rate Limiting

Currently, there are no rate limits implemented. This will be added in future versions.

## Testing

### Using curl

1. Health Check:
```bash
curl http://localhost:8000/api/health/
```

2. Upload PDF:
```bash
# Create a test PDF
echo "%PDF-1.4" > test.pdf
echo "Test content" >> test.pdf

# Upload the PDF
curl -X POST -F "file=@test.pdf" http://localhost:8000/api/upload/
```

### Using Python

```python
import requests

def test_health():
    response = requests.get("http://localhost:8000/api/health/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_upload():
    with open("test.pdf", "rb") as f:
        files = {"file": f}
        response = requests.post("http://localhost:8000/api/upload/", files=files)
        assert response.status_code == 200
        assert "upload_id" in response.json()
```

## Future Endpoints

The following endpoints are planned for future releases:

- `GET /api/uploads/`: List all uploaded files
- `GET /api/uploads/{upload_id}/`: Get details of a specific upload
- `DELETE /api/uploads/{upload_id}/`: Delete an upload
- `POST /api/uploads/{upload_id}/process/`: Process an uploaded file

## Support

If you encounter any issues with the API:

1. Check the [Troubleshooting Guide](../troubleshooting.md)
2. Review the [FAQ](../faq.md)
3. Open an issue in the GitHub repository 