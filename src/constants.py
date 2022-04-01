# Constants for RabbitMQ

RABBIT_MQ_PORT = 5672
RABBIT_MQ_HOST = 'rabbitmq'
RABBIT_MQ_USER = 'guest'
RABBIT_MQ_PASSWORD = 'guest'
RABBIT_MQ_URL = 'amqp://{}:{}@{}:{}'.format(RABBIT_MQ_USER, RABBIT_MQ_PASSWORD, RABBIT_MQ_HOST, RABBIT_MQ_PORT)

TEST_QUEUE = 'test_queue'
MESSAGES_FILE_PATH = './messages_files/messages.json'