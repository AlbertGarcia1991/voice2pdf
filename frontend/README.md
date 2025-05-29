# Voice2PDF Frontend (Vue 3 + Vite)

This is the frontend for the Voice2PDF project, built with Vue 3 and Vite.

## Features

- **PDF Upload**: Upload PDF files to the backend and display upload status and ID.
- **PDF Rendering**: Render each page of the uploaded PDF in the browser using PDF.js.
- **Health Check**: Display backend health status.
- **Comprehensive Unit Tests**: All components are covered by tests using Vitest, including mocks for browser APIs and PDF.js.

## Development Setup

### Prerequisites
- Node.js 20 or later
- npm (comes with Node.js)
- Docker and Docker Compose (for containerized development)

### Local Development

1. Install dependencies:
```bash
npm install
```

2. Start the development server:
```bash
npm run dev
```

The application will be available at [http://localhost:5173](http://localhost:5173).

### Docker Development

1. From the project root, build and start all services:
```bash
docker-compose up --build
```

2. The frontend will be available at [http://localhost:5173](http://localhost:5173).

## Components

### `Upload.vue`
- Allows users to select and upload a PDF file.
- Validates file type (PDF only).
- Uploads the file to the backend (`/api/upload/`).
- Displays upload status, error messages, and the upload ID on success.
- Renders the uploaded PDF using the `Pages` component.

### `Pages.vue`
- Receives a `pdfUrl` prop (blob URL of the PDF file).
- Uses PDF.js to render each page of the PDF as a canvas.
- Handles errors in PDF loading and rendering.

### `HealthCheck.vue`
- Checks the backend health endpoint (`/api/health/`).
- Displays loading, error, or status messages.

## Usage

1. Start the backend and frontend (using either local development or Docker setup).
2. Open the frontend at [http://localhost:5173](http://localhost:5173).
3. Use the upload form to select and upload a PDF file. The file will be sent to the backend and rendered in the browser.
4. The health check component displays the backend status.

## Testing

This project uses [Vitest](https://vitest.dev/) and [@vue/test-utils](https://test-utils.vuejs.org/) for unit testing.

### Run all tests:
```bash
npm test
```

### Test Coverage
- All major components (`Upload.vue`, `Pages.vue`, `HealthCheck.vue`) are covered by tests.
- Tests include mocks for browser APIs (e.g., `URL.createObjectURL`, `canvas`) and PDF.js.
- Error handling and edge cases are tested.

## Docker Configuration

The frontend is containerized using Docker with the following configuration:

- Base image: Node.js 20 (slim)
- Development server runs on port 5173
- Uses volume mounts for hot-reloading during development
- Configured to work with the backend service

### Environment Variables
- `VITE_API_URL`: Backend API URL (default: http://localhost:8000)

---

For more details on the backend and overall project, see the main [README.md](../README.md).
