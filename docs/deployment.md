# Deployment Guide

This guide provides instructions for deploying Voice2PDF to a production environment.

## Prerequisites

- A server with Docker and Docker Compose installed
- Domain name (optional)
- SSL certificate (optional)
- 2GB RAM minimum
- 10GB storage minimum

## Production Setup

### 1. Server Preparation

1. Update system packages:
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. Install Docker and Docker Compose:
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

### 2. Application Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/voice2pdf.git
   cd voice2pdf
   ```

2. Create production environment file:
   ```bash
   cp .env.example .env
   ```

3. Update environment variables:
   ```env
   DEBUG=0
   SECRET_KEY=your-secure-secret-key
   ALLOWED_HOSTS=your-domain.com
   DATABASE_URL=postgres://user:password@db:5432/voice2pdf
   ```

### 3. Database Setup

1. Create a PostgreSQL database:
   ```bash
   docker-compose run --rm django python manage.py migrate
   ```

2. Create a superuser:
   ```bash
   docker-compose run --rm django python manage.py createsuperuser
   ```

### 4. Nginx Configuration

1. Install Nginx:
   ```bash
   sudo apt install nginx
   ```

2. Create Nginx configuration:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:5173;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /api {
           proxy_pass http://localhost:8000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }

       location /media {
           alias /path/to/your/media;
       }

       location /static {
           alias /path/to/your/static;
       }
   }
   ```

3. Enable the configuration:
   ```bash
   sudo ln -s /etc/nginx/sites-available/voice2pdf /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

### 5. SSL Setup

1. Install Certbot:
   ```bash
   sudo apt install certbot python3-certbot-nginx
   ```

2. Obtain SSL certificate:
   ```bash
   sudo certbot --nginx -d your-domain.com
   ```

### 6. Start the Application

1. Build and start containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d --build
   ```

2. Collect static files:
   ```bash
   docker-compose run --rm django python manage.py collectstatic
   ```

## Monitoring

### 1. Log Management

1. View logs:
   ```bash
   docker-compose logs -f
   ```

2. Set up log rotation:
   ```bash
   sudo nano /etc/logrotate.d/voice2pdf
   ```

   Add:
   ```
   /var/log/voice2pdf/*.log {
       daily
       rotate 7
       compress
       delaycompress
       missingok
       notifempty
       create 0640 www-data www-data
   }
   ```

### 2. Performance Monitoring

1. Install monitoring tools:
   ```bash
   docker-compose -f docker-compose.prod.yml -f docker-compose.monitoring.yml up -d
   ```

2. Access monitoring dashboards:
   - Prometheus: http://your-domain.com:9090
   - Grafana: http://your-domain.com:3000

## Backup

### 1. Database Backup

1. Create backup script:
   ```bash
   #!/bin/bash
   BACKUP_DIR="/path/to/backups"
   TIMESTAMP=$(date +%Y%m%d_%H%M%S)
   docker-compose exec -T db pg_dump -U postgres voice2pdf > $BACKUP_DIR/backup_$TIMESTAMP.sql
   ```

2. Set up cron job:
   ```bash
   0 0 * * * /path/to/backup.sh
   ```

### 2. Media Backup

1. Create backup script:
   ```bash
   #!/bin/bash
   BACKUP_DIR="/path/to/backups"
   TIMESTAMP=$(date +%Y%m%d_%H%M%S)
   tar -czf $BACKUP_DIR/media_$TIMESTAMP.tar.gz /path/to/media
   ```

2. Set up cron job:
   ```bash
   0 1 * * * /path/to/media_backup.sh
   ```

## Scaling

### 1. Horizontal Scaling

1. Update docker-compose.prod.yml:
   ```yaml
   services:
     django:
       deploy:
         replicas: 3
   ```

2. Set up load balancer:
   ```nginx
   upstream backend {
       server django1:8000;
       server django2:8000;
       server django3:8000;
   }
   ```

### 2. Vertical Scaling

1. Increase container resources:
   ```yaml
   services:
     django:
       deploy:
         resources:
           limits:
             cpus: '2'
             memory: 2G
   ```

## Maintenance

### 1. Updates

1. Pull latest changes:
   ```bash
   git pull
   ```

2. Rebuild containers:
   ```bash
   docker-compose -f docker-compose.prod.yml up -d --build
   ```

3. Run migrations:
   ```bash
   docker-compose run --rm django python manage.py migrate
   ```

### 2. Security Updates

1. Update system packages:
   ```bash
   sudo apt update
   sudo apt upgrade
   ```

2. Update Docker images:
   ```bash
   docker-compose pull
   docker-compose up -d
   ```

## Troubleshooting

### 1. Common Issues

1. Container won't start:
   ```bash
   docker-compose logs django
   ```

2. Database connection issues:
   ```bash
   docker-compose exec db psql -U postgres -d voice2pdf
   ```

3. Nginx issues:
   ```bash
   sudo nginx -t
   sudo systemctl status nginx
   ```

### 2. Performance Issues

1. Check container resources:
   ```bash
   docker stats
   ```

2. Check database performance:
   ```bash
   docker-compose exec db psql -U postgres -d voice2pdf -c "SELECT * FROM pg_stat_activity;"
   ```

## Support

If you encounter issues:

1. Check the [Troubleshooting Guide](./troubleshooting.md)
2. Review the [FAQ](./faq.md)
3. Open an issue on GitHub
4. Contact the maintainers 