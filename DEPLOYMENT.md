# Deployment Guide for Healthy Dietary Recommendation System

## Table of Contents
1. [Heroku Deployment](#heroku-deployment)
2. [AWS Deployment](#aws-deployment)
3. [Digital Ocean Deployment](#digital-ocean-deployment)
4. [Google Cloud Deployment](#google-cloud-deployment)
5. [Azure Deployment](#azure-deployment)
6. [Production Checklist](#production-checklist)

---

## Heroku Deployment

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git installed

### Steps

1. **Login to Heroku**
   ```bash
   heroku login
   ```

2. **Create Heroku app**
   ```bash
   heroku create your-dietary-app-name
   ```

3. **Add Procfile**
   ```bash
   echo "web: python app.py" > Procfile
   ```

4. **Deploy**
   ```bash
   git push heroku main
   ```

5. **View app**
   ```bash
   heroku open
   ```

6. **View logs**
   ```bash
   heroku logs --tail
   ```

### Cost
- **Free tier**: Limited hours per month
- **Paid**: $7+/month

---

## AWS Deployment

### Option 1: AWS App Runner (Recommended)

1. **Push to GitHub**
   ```bash
   git push origin main
   ```

2. **Go to AWS App Runner console**
   - Select "Create service"
   - Choose "Source code repository"
   - Connect GitHub account
   - Select this repository

3. **Configure**
   - Runtime: Python 3.11
   - Build command: `pip install -r requirements.txt`
   - Start command: `python app.py`

4. **Create and deploy**
   - AWS will automatically build and deploy

### Option 2: EC2 with Docker

1. **Launch EC2 instance**
   - Ubuntu 22.04 LTS
   - t3.micro or larger
   - Open port 5000

2. **SSH into instance**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   ```

3. **Install Docker**
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

4. **Clone and run**
   ```bash
   git clone https://github.com/Skyjhay/dietary-recommendation-system.git
   cd dietary-recommendation-system
   sudo docker-compose up -d
   ```

5. **Set up reverse proxy (Nginx)**
   ```bash
   sudo apt install nginx -y
   sudo nano /etc/nginx/sites-available/default
   ```

   Add this configuration:
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;

       location / {
           proxy_pass http://localhost:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

   Restart Nginx:
   ```bash
   sudo systemctl restart nginx
   ```

### Cost
- **Free tier**: 750 hours/month for 12 months
- **On-demand**: $0.0116/hour for t3.micro

---

## Digital Ocean Deployment

### Prerequisites
- Digital Ocean account
- SSH key generated

### Steps

1. **Create Droplet**
   - Choose Ubuntu 22.04
   - Select 1GB RAM / 1vCPU (minimum)
   - Add SSH key

2. **SSH into Droplet**
   ```bash
   ssh root@your-droplet-ip
   ```

3. **Update system**
   ```bash
   apt update && apt upgrade -y
   ```

4. **Install Docker**
   ```bash
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   ```

5. **Clone repository**
   ```bash
   git clone https://github.com/Skyjhay/dietary-recommendation-system.git
   cd dietary-recommendation-system
   ```

6. **Run with Docker Compose**
   ```bash
   docker-compose up -d
   ```

7. **Set up domain (optional)**
   - Point your domain to the Droplet IP
   - Use Let's Encrypt for SSL

### Cost
- Starting at $4/month

---

## Google Cloud Deployment

### Option 1: Cloud Run (Recommended)

1. **Install Google Cloud SDK**
   ```bash
   curl https://sdk.cloud.google.com | bash
   exec -l $SHELL
   gcloud init
   ```

2. **Set project**
   ```bash
   gcloud config set project YOUR-PROJECT-ID
   ```

3. **Deploy**
   ```bash
   gcloud run deploy dietary-recommendation \
     --source . \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated
   ```

4. **View URL**
   ```bash
   gcloud run services describe dietary-recommendation --region us-central1
   ```

### Option 2: Compute Engine

1. **Create VM instance**
   - Machine type: e2-micro
   - OS: Ubuntu 22.04

2. **SSH and setup (same as AWS EC2)**

### Cost
- **Cloud Run**: $0.00001667 per vCPU-second (free tier: 2M invocations/month)
- **Compute Engine**: Free tier available

---

## Azure Deployment

### Prerequisites
- Azure account
- Azure CLI installed

### Steps

1. **Login to Azure**
   ```bash
   az login
   ```

2. **Create resource group**
   ```bash
   az group create --name dietary-rg --location eastus
   ```

3. **Create App Service Plan**
   ```bash
   az appservice plan create \
     --name dietary-plan \
     --resource-group dietary-rg \
     --sku B1 \
     --is-linux
   ```

4. **Create Web App**
   ```bash
   az webapp create \
     --resource-group dietary-rg \
     --plan dietary-plan \
     --name your-app-name \
     --runtime "PYTHON|3.11"
   ```

5. **Deploy**
   ```bash
   az webapp up \
     --name your-app-name \
     --resource-group dietary-rg
   ```

### Cost
- **Free tier**: Limited (F1)
- **Basic**: $0.0219/hour (B1)

---

## Production Checklist

Before going live, ensure:

- [ ] **Security**
  - [ ] Set `FLASK_ENV=production`
  - [ ] Use strong SECRET_KEY
  - [ ] Enable HTTPS/SSL
  - [ ] Set CORS restrictions
  - [ ] Implement rate limiting
  - [ ] Validate all user inputs

- [ ] **Performance**
  - [ ] Use gunicorn instead of Flask dev server
  - [ ] Enable caching headers
  - [ ] Compress responses
  - [ ] Use CDN for static files
  - [ ] Monitor response times

- [ ] **Reliability**
  - [ ] Set up health checks
  - [ ] Enable auto-restart
  - [ ] Set up monitoring/alerts
  - [ ] Implement error logging
  - [ ] Regular backups

- [ ] **Configuration**
  - [ ] Use environment variables
  - [ ] Document all settings
  - [ ] Test in staging environment
  - [ ] Plan rollback strategy

- [ ] **Documentation**
  - [ ] Document deployment process
  - [ ] Create runbooks
  - [ ] Document API endpoints
  - [ ] Create troubleshooting guide

---

## Production-Ready Gunicorn Setup

1. **Install Gunicorn**
   ```bash
   pip install gunicorn
   ```

2. **Create wsgi.py**
   ```python
   from app import app

   if __name__ == "__main__":
       app.run()
   ```

3. **Run with Gunicorn**
   ```bash
   gunicorn --workers 4 --bind 0.0.0.0:5000 wsgi:app
   ```

4. **Update Dockerfile**
   ```dockerfile
   CMD ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:5000", "wsgi:app"]
   ```

---

## Monitoring & Logging

### Sentry (Error Tracking)
```python
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="YOUR_SENTRY_DSN",
    integrations=[FlaskIntegration()]
)
```

### New Relic (Performance Monitoring)
```python
import newrelic.agent
newrelic.agent.initialize('newrelic.ini')
```

---

## SSL/HTTPS with Let's Encrypt

```bash
# Install Certbot
sudo apt install certbot python3-certbot-nginx -y

# Generate certificate
sudo certbot certonly --standalone -d your-domain.com

# Auto-renew (Nginx)
sudo certbot --nginx -d your-domain.com
```

---

## Support

For deployment issues:
1. Check platform-specific documentation
2. Review application logs
3. Test locally first
4. Create GitHub issue with error details

---

**Happy deploying!** 🚀
