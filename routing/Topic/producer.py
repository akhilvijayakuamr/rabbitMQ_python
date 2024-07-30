import pika
from pika.exchange_type import ExchangeType

connection_parameters =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange='mytopicex', exchange_type=ExchangeType.topic)

user_payment_message = "The urope user pay something you"

channel.basic_publish(exchange='mytopicex', routing_key='user.europe.payment', body=user_payment_message)



bussines_payment_message = "This is bussiness message from your partener"

channel.basic_publish(exchange='mytopicex', routing_key='pay.user.europe', body=bussines_payment_message)

print("The producer is sent message")

connection.close()