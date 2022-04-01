import logging
import time
import pika
import json
from constants import *

logging.basicConfig(level = logging.INFO)

# Read messages from file
with open(MESSAGES_FILE_PATH, 'r') as f:
  messages_dict = json.load(f)

# Sleep for 20 seconds to allow RabbitMQ to come up
logging.info('Sleeping for 20 seconds to allow RabbitMQ to come up')
time.sleep(20)

params = pika.URLParameters(RABBIT_MQ_URL)
connection = pika.BlockingConnection(params)

# Start a communication channel
channel = connection.channel()
# Create TEST_QUEUE
channel.queue_declare(queue=TEST_QUEUE) 

# Publish messages to TEST_QUEUE
try: 
  for message in messages_dict:
    channel.basic_publish(exchange='', routing_key=TEST_QUEUE, body=json.dumps(message))
    logging.info('Published message: {}'.format(str(message)))
except Exception as e:
  logging.error('Error publishing message: {}'.format(str(e)))

connection.close()
logging.info('Connection closed')