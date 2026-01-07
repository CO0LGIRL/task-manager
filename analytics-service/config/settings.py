import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'analytics-secret'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'rest_framework',
    'apps.analytics',
]

CLICKHOUSE_CONFIG = {
    'host': 'clickhouse',
    'port': 9000,
    'user': 'default', 
    'password': '',
    'database': 'analytics'
}

KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'kafka:29092')