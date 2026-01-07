from django.core.management.base import BaseCommand
from apps.analytics.consumers import start_kafka_consumer

class Command(BaseCommand):
    help = 'Starts the Kafka consumer for analytics'

    def handle(self, *args, **options):
        start_kafka_consumer()