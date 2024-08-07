import pika
from pika.exchange_type import ExchangeType

connection_parameters =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='routing', exchange_type=ExchangeType.direct)

message = "This message need to be routing"

channel.basic_publish(exchange='routing', routing_key='paymentonly', body=message)

print(f"sent message: {message}")

connection.close()