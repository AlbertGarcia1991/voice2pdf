# Troubleshooting Guide

This guide covers common issues you might encounter while working with Voice2PDF and their solutions.

## Docker Issues

### Container Won't Start

**Error**: `Error starting userland proxy: listen tcp 0.0.0.0:8000: bind: address already in use`

**Solution**:
1. Check if another process is using port 8000:
   ```bash
   # On macOS/Linux
   lsof -i :8000
   
   # On Windows
   netstat -ano | findstr :8000
   ```
2. Stop the process or change the port in `docker-compose.yml`

### Docker Compose Build Fails

**Error**: `ERROR: Service 'django' failed to build`

**Solution**:
1. Check Docker logs:
   ```bash
   docker-compose logs django
   ```
2. Ensure all required files exist:
   ```bash
   ls backend/
   ```
3. Try rebuilding with no cache:
   ```bash
   docker-compose build --no-cache
   ```

## Django Issues

### Database Migration Errors

**Error**: `django.db.utils.OperationalError: could not connect to server`

**Solution**:
1. Ensure the database container is running:
   ```bash
   docker-compose ps
   ```
2. Try running migrations manually:
   ```bash
   docker-compose run --rm django python manage.py migrate
   ```

### WSGI Application Error

**Error**: `ModuleNotFoundError: No module named 'backend.wsgi'`

**Solution**:
1. Check if the WSGI file exists:
   ```bash
   ls backend/backend/wsgi.py
   ```
2. Ensure the correct settings module is set:
   ```bash
   export DJANGO_SETTINGS_MODULE=backend.settings
   ```

## API Issues

### File Upload Fails

**Error**: `Only PDF files are allowed`

**Solution**:
1. Verify the file is a valid PDF:
   ```bash
   file test.pdf
   ```
2. Check the file size (should be less than 10MB)
3. Ensure the correct content type is set:
   ```bash
   curl -X POST -F "file=@test.pdf" -H "Content-Type: multipart/form-data" http://localhost:8000/api/upload/
   ```

### Health Check Fails

**Error**: `Failed to connect to localhost port 8000`

**Solution**:
1. Check if the server is running:
   ```bash
   docker-compose ps
   ```
2. Check server logs:
   ```bash
   docker-compose logs django
   ```
3. Try restarting the containers:
   ```bash
   docker-compose down
   docker-compose up --build
   ```

## Development Environment Issues

### Python Virtual Environment

**Error**: `ModuleNotFoundError: No module named 'django'`

**Solution**:
1. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Node.js Issues

**Error**: `npm install` fails

**Solution**:
1. Clear npm cache:
   ```bash
   npm cache clean --force
   ```
2. Delete node_modules and reinstall:
   ```bash
   rm -rf node_modules
   npm install
   ```

## Common Questions

### How to Reset Everything?

```bash
# Stop all containers
docker-compose down

# Remove all containers and volumes
docker-compose down -v

# Remove all images
docker-compose down --rmi all

# Rebuild and start
docker-compose up --build
```

### How to View Logs?

```bash
# All services
docker-compose logs

# Specific service
docker-compose logs django

# Follow logs
docker-compose logs -f
```

### How to Access the Database?

```bash
# Using psql
docker-compose exec db psql -U postgres

# Using Django shell
docker-compose run --rm django python manage.py shell
```

## Getting Help

If you're still experiencing issues:

1. Check the [FAQ](./faq.md)
2. Search existing issues on GitHub
3. Create a new issue with:
   - Error message
   - Steps to reproduce
   - Environment details
   - Relevant logs

## Debugging Tips

1. Enable Django debug mode:
   ```python
   DEBUG = True
   ```

2. Check Django logs:
   ```bash
   docker-compose logs django
   ```

3. Use Django debug toolbar:
   ```python
   INSTALLED_APPS += ['debug_toolbar']
   ```

4. Check browser console for frontend issues

5. Use Django shell for debugging:
   ```bash
   docker-compose run --rm django python manage.py shell
   ``` 