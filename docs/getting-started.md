# Getting Started with Voice2PDF

This guide will help you get up and running with Voice2PDF quickly.

## Project Overview

Voice2PDF is a web application that allows users to upload PDF files and process them. The application consists of two main components:

- **Backend**: A Django REST Framework API that handles file uploads and processing
- **Frontend**: A React-based web interface for user interaction

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.11 or higher
- Node.js 18 or higher
- Docker and Docker Compose
- Git

## Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/voice2pdf.git
cd voice2pdf
```

### 2. Backend Setup

#### Using Docker (Recommended)

```bash
cd backend
docker-compose up --build
```

This will:
- Build the Docker image
- Install all Python dependencies
- Run database migrations
- Start the Django development server

#### Manual Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 3. Frontend Setup

#### Using Docker (Recommended)

The frontend will be automatically started with the backend when using Docker Compose.

#### Manual Setup

```bash
cd frontend
npm install
npm run dev
```

## Quick Start

1. Start the application:
   ```bash
   docker-compose up --build
   ```

2. Access the application:
   - Frontend: http://localhost:5173
   - Backend API: http://localhost:8000

3. Test the API:
   ```bash
   # Health check
   curl http://localhost:8000/api/health/

   # Upload a PDF
   curl -X POST -F "file=@test.pdf" http://localhost:8000/api/upload/
   ```

## Configuration

### Environment Variables

Create a `.env` file in the backend directory:

```env
DEBUG=1
DJANGO_SETTINGS_MODULE=backend.settings
```

### Media Storage

By default, uploaded files are stored in the `media` directory. You can configure this in `backend/backend/settings.py`.

## Next Steps

- Read the [Architecture Documentation](./architecture.md) to understand the system design
- Check the [API Documentation](./api/README.md) for available endpoints
- Review the [Development Guide](./development.md) for contributing guidelines

## Common Issues

If you encounter any issues during setup:

1. Ensure all prerequisites are installed
2. Check the [Troubleshooting Guide](./troubleshooting.md)
3. Verify Docker is running properly
4. Check the logs:
   ```bash
   docker-compose logs
   ```

## Support

If you need help:
1. Check the [FAQ](./faq.md)
2. Open an issue in the GitHub repository
3. Review the [Troubleshooting Guide](./troubleshooting.md) 