# Mandai Backend

A Django-based web scraping application for commodity prices with vendor and market management.

## Features
- Automated web scraping of commodity prices using Selenium
- Scheduled scraping tasks with Celery
- CRUD operations for vendors and markets
- Data persistence with Django ORM
- API endpoints for data access
- Redis integration for task queue management

## Tech Stack
- Django
- Celery
- Redis
- Selenium
- Docker

## Prerequisites
- Python 3.8+
- Redis Instance

## Setup & Installation

1. Clone the repository
```bash
git clone https://github.com/yogesh-bhandare/mandai-backend-api.git
cd mandai-backend-api
```

2. Create virtual environment
For MacOS/Linux/Windows::
```bash
python3 -m venv venv
source venv/bin/activate
```
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Redis Setup
Using Docker:
This will start Redis on redis://localhost:6170
```bash
docker compose -f compose.yaml up -d
```

5. Environment Configuration
Create .env in project root:
```bash
CELERY_BROKER_REDIS_URL="redis://localhost:6170"
DEBUG=True
```

6. Database Setup
```bash
python manage.py migrate
```

7. Start Services
In separate terminals:
```bash
# Terminal 1: Django Server
python manage.py runserver

# Terminal 2: Celery Worker & Beat
celery -A mandai worker --beat
```