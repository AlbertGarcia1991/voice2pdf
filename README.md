# Voice2PDF

A web application that allows users to upload PDF files and convert them to text using voice recognition.

## Project Overview

Voice2PDF consists of two main components:
- **Frontend**: Vue 3 application with PDF upload and rendering capabilities
- **Backend**: Django REST API for handling file uploads and processing

## Prerequisites

- Node.js 20 or later
- Python 3.8 or later
- Docker and Docker Compose (for containerized development)
- Git
- pre-commit (for development)

## Quick Start with Docker

1. Clone the repository:
```bash
git clone https://github.com/yourusername/voice2pdf.git
cd voice2pdf
```

2. Build and start the services:
```bash
docker-compose up --build
```

3. Access the application:
- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend API: [http://localhost:8000](http://localhost:8000)

## Development Setup

### Pre-commit Hooks Setup

1. Install pre-commit:
```bash
pip install pre-commit
```

2. Install the pre-commit hooks:
```bash
pre-commit install
```

This will automatically run flake8 and other checks before each commit, preventing code style issues from being pushed to the repository.

### Frontend Development

See [frontend/README.md](frontend/README.md) for detailed frontend setup and development instructions.

### Backend Development

1. Create and activate a virtual environment:
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

The backend API will be available at [http://localhost:8000](http://localhost:8000).

## Project Structure

```
voice2pdf/
├── frontend/           # Vue 3 frontend application
│   ├── src/
│   │   ├── components/ # Vue components
│   │   └── ...
│   ├── Dockerfile
│   └── package.json
├── backend/           # Django backend application
│   ├── backend/      # Django project settings
│   ├── api/          # API endpoints
│   ├── Dockerfile
│   └── requirements.txt
└── docker-compose.yml
```

## Features

### Frontend
- PDF file upload with drag-and-drop support
- PDF preview with page-by-page rendering
- Real-time upload status and error handling
- Backend health check monitoring

### Backend
- RESTful API for file uploads
- PDF file processing and storage
- Health check endpoint
- CORS configuration for frontend communication

## API Endpoints

- `POST /api/upload/`: Upload PDF files
- `GET /api/health/`: Check backend health status

## Testing

### Frontend Tests
```bash
cd frontend
npm test
```

### Backend Tests
```bash
cd backend
python manage.py test
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Install pre-commit hooks (see Development Setup)
4. Commit your changes
5. Push to the branch
6. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 