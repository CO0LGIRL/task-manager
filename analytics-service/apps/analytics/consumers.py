import json
import logging
from confluent_kafka import Consumer, KafkaError
from django.conf import settings
from .models import db

logger = logging.getLogger(__name__)

def start_kafka_consumer():
    c = Consumer({
        'bootstrap.servers': settings.KAFKA_BOOTSTRAP_SERVERS,
        'group.id': 'analytics_group',
        'auto.offset.reset': 'earliest'
    })

    c.subscribe(['analytics_events'])

    logger.info("Kafka Consumer started...")

    try:
        while True:
            msg = c.poll(1.0)

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    logger.error(msg.error())
                    break

            try:
                data = json.loads(msg.value().decode('utf-8'))
                logger.info(f"Received event: {data.get('event_type')}")
                
                db.insert_event(data)
                
            except Exception as e:
                logger.error(f"Error processing message: {e}")

    except KeyboardInterrupt:
        pass
    finally:
        c.close()