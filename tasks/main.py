import dramatiq
from dramatiq.brokers.rabbitmq import RabbitmqBroker

rabbitmq_broker = RabbitmqBroker(url="amqp://guest:guest@rabbitmq:5672/")
dramatiq.set_broker(rabbitmq_broker)


@dramatiq.actor
def process_data(data):
    print(f"Processing data: {data}")
