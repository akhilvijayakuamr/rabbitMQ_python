import pika
from pika.exchange_type import ExchangeType

def on_message_received(ch, method, properties, body):
    print(f"received message {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)

channel.queue_declare(queue='letterheaders')

bind_args ={
    'x-match':'any',
    'name':'akhil',
    'age':'24'
}

channel.queue_bind(queue='letterheaders', exchange='headersexchange', arguments=bind_args)

channel.basic_consume(queue='letterheaders', auto_ack=True, on_message_callback=on_message_received)


print("Start consuming messages")

channel.start_consuming()