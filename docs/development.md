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