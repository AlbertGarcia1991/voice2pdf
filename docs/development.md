# Development Guide

This guide provides detailed information for developers who want to contribute to Voice2PDF.

## Development Environment Setup

### Prerequisites

- Python 3.11 or higher
- Node.js 18 or higher
- Git
- Docker and Docker Compose (optional)
- A code editor (VS Code recommended)

### Backend Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   export DEBUG=1
   export DJANGO_SETTINGS_MODULE=backend.settings
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

## Code Style

### Python

We follow PEP 8 guidelines. Use the following tools:

1. Flake8 for linting:
   ```bash
   flake8
   ```

2. Black for formatting:
   ```bash
   black .
   ```

3. isort for import sorting:
   ```bash
   isort .
   ```

### JavaScript/TypeScript

We use ESLint and Prettier:

1. Lint code:
   ```bash
   npm run lint
   ```

2. Format code:
   ```bash
   npm run format
   ```

## Testing

### Backend Tests

1. Run all tests:
   ```bash
   python manage.py test
   ```

2. Run specific tests:
   ```bash
   python manage.py test apps.upload.tests
   ```

3. Run with coverage:
   ```bash
   coverage run manage.py test
   coverage report
   ```

### Frontend Tests

1. Run unit tests:
   ```bash
   npm test
   ```

2. Run with coverage:
   ```bash
   npm run test:coverage
   ```

## Git Workflow

1. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes

3. Run tests and linting:
   ```bash
   # Backend
   flake8
   black .
   isort .
   python manage.py test

   # Frontend
   npm run lint
   npm test
   ```

4. Commit your changes:
   ```bash
   git add .
   git commit -m "feat: your feature description"
   ```

5. Push to remote:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Create a pull request

## Adding New Features

### Backend

1. Create a new app:
   ```bash
   python manage.py startapp your_app_name
   ```

2. Add the app to `INSTALLED_APPS` in `settings.py`

3. Create models in `models.py`

4. Create migrations:
   ```bash
   python manage.py makemigrations
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Create views in `views.py`

7. Add URLs in `urls.py`

8. Write tests in `tests.py`

### Frontend

1. Create new components in `src/components`

2. Add new pages in `src/pages`

3. Update routing in `src/App.tsx`

4. Add new API calls in `src/api`

5. Write tests in `__tests__` directory

### Data Models

### Template and Field (templates app)

The `templates` app provides a flexible way to store PDF form templates and their fields. It includes:
- `Template`: Represents a PDF template, linked to an upload.
- `Field`: Represents a form field on a template, with type, label, position, validation, and value.

#### Example Model Definition
```python
class Template(models.Model):
    upload_id = models.CharField(max_length=64, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Field(models.Model):
    template = models.ForeignKey('Template', related_name='fields', on_delete=models.CASCADE)
    field_id = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    label = models.CharField(max_length=128)
    placeholder = models.CharField(max_length=256, blank=True)
    page_number = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    validation = models.JSONField(default=dict)
    value = models.TextField(blank=True)
```

## Serializers

### Template and Field Serializers

The `TemplateSerializer` and `FieldSerializer` in `templates/serializers.py` support full (de)serialization of templates and their nested fields, including creation and update of nested objects.

#### Example Usage
```python
serializer = TemplateSerializer(template_instance)
data = serializer.data  # Nested fields included

# Deserialization
serializer = TemplateSerializer(data=payload)
serializer.is_valid()
serializer.save()
```

## Testing

- The `templates` app is fully test-driven: see `templates/tests/test_models_serializers.py` for model and serializer tests.
- Tests cover creation, serialization, and deserialization of templates and fields.

## Adding New Features

### Example: Adding a Template Data Model (TDD)

1. **Write tests first** for the new model and serializer in `templates/tests/`.
2. **Implement models** in `templates/models.py`.
3. **Implement serializers** in `templates/serializers.py`.
4. **Run tests** with `pytest` and ensure all pass before proceeding.
5. Only then, add endpoints or business logic.

This approach ensures robust, well-tested code for all new features.

## Debugging

### Backend

1. Use Django debug toolbar:
   ```python
   INSTALLED_APPS += ['debug_toolbar']
   ```

2. Use Django shell:
   ```bash
   python manage.py shell
   ```

3. Check logs:
   ```bash
   tail -f logs/django.log
   ```

### Frontend

1. Use browser developer tools

2. Use React Developer Tools

3. Check console logs

## Documentation

### Code Documentation

1. Use docstrings for Python:
   ```python
   def your_function():
       """
       Function description.

       Args:
           param1: Description of param1
           param2: Description of param2

       Returns:
           Description of return value
       """
   ```

2. Use JSDoc for JavaScript:
   ```javascript
   /**
    * Function description
    * @param {string} param1 - Description of param1
    * @param {number} param2 - Description of param2
    * @returns {boolean} Description of return value
    */
   ```

### API Documentation

Update the [API Documentation](./api/README.md) when adding new endpoints.

## Performance Optimization

### Backend

1. Use Django Debug Toolbar to identify slow queries

2. Add database indexes:
   ```python
   class Meta:
       indexes = [
           models.Index(fields=['field_name']),
       ]
   ```

3. Use caching:
   ```python
   from django.core.cache import cache

   cache.set('key', value, timeout=3600)
   cache.get('key')
   ```

### Frontend

1. Use React.memo for expensive components

2. Implement lazy loading:
   ```javascript
   const LazyComponent = React.lazy(() => import('./LazyComponent'));
   ```

3. Optimize images and assets

## Security

1. Never commit sensitive data

2. Use environment variables:
   ```python
   import os
   SECRET_KEY = os.environ.get('SECRET_KEY')
   ```

3. Validate user input

4. Use HTTPS in production

## Deployment

See the [Deployment Guide](./deployment.md) for detailed instructions.

## Getting Help

1. Check the [Troubleshooting Guide](./troubleshooting.md)

2. Review the [FAQ](./faq.md)

3. Open an issue on GitHub

4. Contact the maintainers

## Makefile Commands

The project includes a Makefile with various commands to help with development tasks. Here's a comprehensive guide to all available commands.

### Getting Started

To see all available commands and their descriptions:
```bash
make help
```

### Docker Commands

| Command | Description |
|---------|-------------|
| `make up` | Start all services in the foreground |
| `make up-d` | Start all services in detached mode (background) |
| `make down` | Stop all running services |
| `make build` | Build all Docker services |
| `make rebuild` | Rebuild all Docker services without using cache |

### Frontend Commands

| Command | Description |
|---------|-------------|
| `make frontend-install` | Install frontend dependencies |
| `make frontend-dev` | Start frontend development server |
| `make frontend-test` | Run frontend tests |
| `make frontend-lint` | Run frontend linter |

### Backend Commands

| Command | Description |
|---------|-------------|
| `make backend-install` | Install backend dependencies |
| `make backend-migrate` | Run database migrations |
| `make backend-test` | Run backend tests |
| `make backend-lint` | Run backend linter |

### Development Workflow

| Command | Description |
|---------|-------------|
| `make setup` | Install all dependencies (frontend and backend) |
| `make test` | Run all tests (frontend and backend) |
| `make lint` | Run all linters (frontend and backend) |
| `make dev` | Start the complete development environment |
| `make clean` | Clean up temporary files and containers |

### Development Environment

To start the development environment:
```bash
make dev
```

This will:
1. Start all services in detached mode
2. Make the frontend available at http://localhost:5173
3. Make the backend available at http://localhost:8000

### Running Modes

The project supports two main running modes:

#### Detached Mode (`make dev`)
- Starts services in the background
- Doesn't block your terminal
- Perfect for development as you can run other commands
- Services keep running until explicitly stopped
- Use this mode for regular development work
- To view logs: `docker compose logs -f`

#### Foreground Mode (`make up`)
- Starts services in the foreground
- Shows real-time logs in your terminal
- Blocks the terminal (can't run other commands)
- Stops when you press Ctrl+C
- Useful for debugging and monitoring
- Perfect for troubleshooting issues

Choose the mode based on your needs:
- Use `make dev` for regular development
- Use `make up` when you need to debug or monitor services closely

### Cleanup

To clean up the development environment:
```bash
make clean
```

This command will:
1. Stop all running services
2. Remove all containers and volumes
3. Clean up temporary files including:
   - Python cache files
   - Node modules
   - Test coverage files
   - Build artifacts
   - Cache directories

### Best Practices

1. Always run `make setup` when first cloning the repository
2. Use `make dev` to start the development environment
3. Run `make test` before committing changes
4. Use `make lint` to ensure code quality
5. Run `make clean` when switching branches or when you encounter issues

### Troubleshooting

If you encounter issues:
1. Run `make clean` to ensure a clean state
2. Run `make rebuild` to rebuild all services
3. Check the logs using `docker compose logs`
4. Ensure all dependencies are installed with `make setup`

## API Endpoints

### Template Endpoints (templates app)

- **Create Template**
  - `POST /api/templates/`
  - Request body: JSON with `upload_id` and a list of `fields` (see below)
  - Response: `{ "template_id": <id> }` (201 Created)

- **Retrieve Template**
  - `GET /api/templates/<id>/`
  - Response: Full template object with nested fields (200 OK)

#### Example: Create Template
```json
POST /api/templates/
{
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
      "validation": {"required": true},
      "value": "John Doe"
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
      "value": "25"
    }
  ]
}
```
Response:
```json
{
  "template_id": 1
}
```

#### Example: Retrieve Template
```http
GET /api/templates/1/
```
Response:
```json
{
  "id": 1,
  "upload_id": "test-upload-789",
  "created_at": "2024-06-01T12:34:56.789Z",
  "fields": [
    {
      "id": 1,
      "template": 1,
      "field_id": "field1",
      "type": "text",
      "label": "Name",
      "placeholder": "Enter your name",
      "page_number": 1,
      "x": 100.0,
      "y": 200.0,
      "width": 300.0,
      "height": 50.0,
      "validation": {"required": true},
      "value": "John Doe"
    },
    {
      "id": 2,
      "template": 1,
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
      "value": "25"
    }
  ]
}
```

### TDD Workflow Note

- The template endpoints were developed using TDD: endpoint tests were written first, then the views and URLs were implemented, and all tests were run to confirm correctness.
