# Voice2PDF

A full-stack application with Django backend and Vue.js frontend.

## Project Structure

```
.
├── backend/             # Django backend
│   ├── app/            # Django app
│   ├── tests/          # Backend tests
│   ├── Dockerfile      # Backend Dockerfile
│   └── requirements.txt # Python dependencies
├── frontend/           # Vue.js frontend
│   ├── src/           # Source files
│   ├── Dockerfile     # Frontend Dockerfile
│   └── package.json   # Node dependencies
└── docker-compose.yml # Docker orchestration
```

## Prerequisites

- Docker
- Docker Compose

## Getting Started

1. Clone the repository
2. Run the application:
   ```bash
   docker-compose up --build
   ```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000

## Development

### Backend

The Django backend provides a REST API with the following endpoints:
- `GET /api/health/` - Health check endpoint

### Frontend

The Vue.js frontend includes:
- Health check component that displays backend status
- Jest tests for components

## Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
``` 