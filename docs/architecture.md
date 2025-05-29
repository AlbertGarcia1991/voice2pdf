# Architecture Documentation

This document provides a detailed overview of the Voice2PDF system architecture.

## System Overview

Voice2PDF is a web application that allows users to upload and process PDF files. The system consists of several components:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Frontend  │     │   Backend   │     │  Database   │
│  (React)    │◄────┤  (Django)   │◄────┤ (PostgreSQL)│
└─────────────┘     └─────────────┘     └─────────────┘
       ▲                   ▲
       │                   │
       ▼                   ▼
┌─────────────┐     ┌─────────────┐
│    Nginx    │     │    Media    │
│  (Reverse   │     │  Storage    │
│   Proxy)    │     │             │
└─────────────┘     └─────────────┘
```

## Component Details

### 1. Frontend (React)

The frontend is built with React and provides the user interface.

#### Key Features:
- File upload interface
- Progress tracking
- Error handling
- Responsive design

#### Directory Structure:
```
frontend/
├── src/
│   ├── components/    # Reusable UI components
│   ├── pages/         # Page components
│   ├── api/           # API integration
│   ├── hooks/         # Custom React hooks
│   ├── utils/         # Utility functions
│   └── App.tsx        # Main application component
├── public/            # Static assets
└── package.json       # Dependencies and scripts
```

### 2. Backend (Django)

The backend is built with Django and Django REST Framework.

#### Key Features:
- RESTful API
- File validation
- PDF processing
- Database management

#### Directory Structure:
```
backend/
├── backend/            # Project settings
│   ├── settings.py     # Django settings
│   ├── urls.py         # URL routing
│   └── wsgi.py         # WSGI configuration
├── apps/               # Django applications
│   └── upload/         # Upload handling
│       ├── models.py   # Database models
│       ├── views.py    # API views
│       ├── urls.py     # URL patterns
│       └── tests.py    # Test cases
└── manage.py           # Django management script
```

### 3. Database (PostgreSQL)

PostgreSQL is used for data persistence.

#### Schema:
```sql
CREATE TABLE uploads (
    id UUID PRIMARY KEY,
    file_name VARCHAR(255),
    file_path VARCHAR(255),
    upload_date TIMESTAMP,
    status VARCHAR(50),
    pages JSONB
);
```

### 4. Media Storage

Files are stored in the `media` directory.

#### Structure:
```
media/
├── uploads/         # Uploaded files
│   └── YYYY/MM/DD/  # Organized by date
└── processed/       # Processed files
```

## Data Flow

1. **File Upload**:
   ```
   User → Frontend → Backend → Media Storage
   ```

2. **File Processing**:
   ```
   Backend → PDF Processing → Database Update
   ```

3. **Status Update**:
   ```
   Backend → Database → Frontend → User
   ```

## API Endpoints

### 1. Health Check
```http
GET /api/health/
```

### 2. File Upload
```http
POST /api/upload/
```

## Security

### 1. File Validation
- File type checking
- Size limits
- Content validation

### 2. API Security
- CORS configuration
- Rate limiting
- Input validation

## Performance Considerations

### 1. Caching
- Static file caching
- API response caching
- Database query caching

### 2. Asynchronous Processing
- File upload handling
- PDF processing
- Status updates

## Scalability

### 1. Horizontal Scaling
- Multiple backend instances
- Load balancing
- Database replication

### 2. Vertical Scaling
- Resource allocation
- Performance optimization
- Database tuning

## Monitoring

### 1. Application Metrics
- Request latency
- Error rates
- Resource usage

### 2. System Metrics
- CPU usage
- Memory usage
- Disk I/O

## Deployment

### 1. Development
- Docker Compose
- Local database
- Debug mode

### 2. Production
- Nginx reverse proxy
- SSL/TLS
- Production database

## Future Improvements

### 1. Planned Features
- User authentication
- File versioning
- Advanced PDF processing

### 2. Technical Improvements
- Microservices architecture
- Message queue integration
- Cloud storage integration

## Dependencies

### 1. Frontend
- React
- TypeScript
- Vite
- Axios

### 2. Backend
- Django
- Django REST Framework
- PostgreSQL
- Python PDF libraries

## Development Workflow

1. **Local Development**:
   ```bash
   docker-compose up
   ```

2. **Testing**:
   ```bash
   # Backend
   python manage.py test
   
   # Frontend
   npm test
   ```

3. **Deployment**:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## Support

For more information:
1. Check the [API Documentation](./api/README.md)
2. Review the [Deployment Guide](./deployment.md)
3. Read the [Development Guide](./development.md) 