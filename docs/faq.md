# Frequently Asked Questions (FAQ)

## General Questions

### What is Voice2PDF?

Voice2PDF is a web application that allows users to upload PDF files and process them. It provides a REST API for file uploads and a web interface for user interaction.

### What are the system requirements?

- Python 3.11 or higher
- Node.js 18 or higher
- Docker and Docker Compose
- 2GB RAM minimum
- 1GB free disk space

### Is this project open source?

Yes, Voice2PDF is open source and available under the MIT license.

## Installation

### How do I install Voice2PDF?

See the [Getting Started Guide](./getting-started.md) for detailed installation instructions.

### Can I run Voice2PDF without Docker?

Yes, you can run the application without Docker. See the [Development Guide](./development.md) for manual setup instructions.

### What ports does Voice2PDF use?

- Backend API: 8000
- Frontend: 5173
- Database: 5432

## Usage

### How do I upload a PDF?

You can upload PDFs in several ways:

1. Using the web interface at http://localhost:5173
2. Using curl:
   ```bash
   curl -X POST -F "file=@test.pdf" http://localhost:8000/api/upload/
   ```
3. Using Python:
   ```python
   import requests
   response = requests.post("http://localhost:8000/api/upload/", files={"file": open("test.pdf", "rb")})
   ```

### What file types are supported?

Currently, only PDF files are supported. The API will return an error for any other file type.

### What is the maximum file size?

The default maximum file size is 10MB. This can be configured in the Django settings.

## Development

### How do I contribute to the project?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

See the [Contributing Guide](./contributing.md) for more details.

### How do I run the tests?

```bash
# Backend tests
cd backend
python manage.py test

# Frontend tests
cd frontend
npm test
```

### How do I add new features?

1. Create a new branch
2. Implement the feature
3. Add tests
4. Update documentation
5. Submit a pull request

## Troubleshooting

### The server won't start

1. Check if the required ports are available
2. Ensure Docker is running
3. Check the logs:
   ```bash
   docker-compose logs
   ```

### File uploads fail

1. Verify the file is a valid PDF
2. Check the file size
3. Ensure the correct content type is set
4. Check the server logs

### Database connection issues

1. Ensure the database container is running
2. Check database logs
3. Verify database credentials

## Security

### Is the API secure?

The API currently doesn't implement authentication. This will be added in future versions.

### How are files stored?

Files are stored in the `media` directory by default. In production, you should configure a proper storage backend.

### Are there rate limits?

Currently, there are no rate limits. This will be implemented in future versions.

## Performance

### How many files can I upload?

There is no hard limit, but consider:
- Available disk space
- Server resources
- Network bandwidth

### How do I optimize performance?

1. Use a production-grade web server (e.g., Nginx)
2. Configure proper caching
3. Use a CDN for static files
4. Optimize database queries

## Support

### Where can I get help?

1. Check the [Troubleshooting Guide](./troubleshooting.md)
2. Review the [Documentation](./README.md)
3. Open an issue on GitHub
4. Contact the maintainers

### How do I report bugs?

1. Check if the bug is already reported
2. Create a new issue with:
   - Clear description
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details
   - Relevant logs

### How do I request features?

1. Check if the feature is already requested
2. Create a new issue with:
   - Feature description
   - Use case
   - Potential implementation
   - Benefits 