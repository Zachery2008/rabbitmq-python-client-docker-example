import logging
import pika
import json

class rabbitmq_client:
  def __init__(self, url: str):
    params = pika.URLParameters(url)
    connection = pika.BlockingConnection(params)
    # Start a communication channel
    self.client = connection.channel()

  def create_queue(self, queue_name: str) -> None:
    self.client.queue_declare(queue=queue_name)
    logging.info('Created queue: {}'.format(queue_name))
  
  def publish_message(self, queue_name: str, message: dict) -> None:
    self.client.basic_publish(exchange='', routing_key=queue_name, body=json.dumps(message))
    logging.info('Published message: {}'.format(message))

  def close(self) -> None:
    self.client.close()
    logging.info('Connection closed')