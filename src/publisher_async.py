import logging
import time
import json
import asyncio
from constants import *
from rabbitmq_async_client import rabbitmq_async_client

logging.basicConfig(level = logging.INFO)

async def main() -> None:

  # Read messages from file
  with open(MESSAGES_FILE_PATH, 'r') as f:
    messages_dict = json.load(f)

  # Sleep for 20 seconds to allow RabbitMQ to come up
  logging.info('Sleeping for 20 seconds to allow RabbitMQ to come up')
  time.sleep(20)

  rabbitmq_client = rabbitmq_async_client(RABBIT_MQ_URL)

  # Create TEST_QUEUE
  await rabbitmq_client.create_queue(TEST_QUEUE) 

  # Publish messages to TEST_QUEUE
  try: 
    await asyncio.gather(*[rabbitmq_client.publish_message(TEST_QUEUE, message) for message in messages_dict])
  except Exception as e:
    logging.error('Error publishing message: {}'.format(str(e)))

  await rabbitmq_client.close()

if __name__ == "__main__":
    asyncio.run(main())