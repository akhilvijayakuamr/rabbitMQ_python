import pika
from pika.exchange_type import ExchangeType

connection_parameters =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type=ExchangeType.headers)

message = "This is my header exchange"

channel.basic_publish(exchange='headersexchange',
                      routing_key='',
                      body=message,
                      properties=pika.BasicProperties(headers={'name':'akhil'}))

print(f"sent message: {message}")

connection.close()