import json
import logging
from confluent_kafka import Producer
from django.conf import settings

logger = logging.getLogger(__name__)

class EventProducer:
    def __init__(self):
        self._producer = None

    @property
    def client(self):
        if self._producer is None:
            try:
                self._producer = Producer({
                    'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
                    'client.id': 'api-service-producer',
                    'socket.timeout.ms': 1000, 
                })
            except Exception as e:
                logger.error(f"Kafka Producer init error: {e}")
        return self._producer

    def send_event(self, topic: str, value: dict):
        client = self.client
        if not client:
            logger.error("Producer not available, event dropped")
            return

        try:
            client.produce(
                topic,
                value=json.dumps(value).encode('utf-8'),
                callback=self.delivery_report
            )
            client.flush(timeout=1.0)
        except Exception as e:
            logger.error(f"Failed to send event: {e}")

    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            logger.error(f'Message delivery failed: {err}')

producer = EventProducer()