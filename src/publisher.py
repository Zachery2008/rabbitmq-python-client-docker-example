import logging
import time
import pika
import json
from constants import *
from rabbitmq_client import rabbitmq_client

logging.basicConfig(level = logging.INFO)

# Read messages from file
with open(MESSAGES_FILE_PATH, 'r') as f:
  messages_dict = json.load(f)

# Sleep for 20 seconds to allow RabbitMQ to come up
logging.info('Sleeping for 20 seconds to allow RabbitMQ to come up')
time.sleep(20)

rabbitmq_client = rabbitmq_client(RABBIT_MQ_URL)

# Create TEST_QUEUE
rabbitmq_client.create_queue(TEST_QUEUE) 

# Publish messages to TEST_QUEUE
try: 
  for message in messages_dict:
    rabbitmq_client.publish_message(TEST_QUEUE, message)
except Exception as e:
  logging.error('Error publishing message: {}'.format(str(e)))

rabbitmq_client.close()