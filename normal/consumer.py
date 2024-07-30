import pika


def on_message_received(ch, method, properties, body):
    print(f"received message {body}")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()


channel.queue_declare(queue='letter')

channel.basic_consume(queue='letter', auto_ack=True, on_message_callback=on_message_received)


print("Start consuming messages")

channel.start_consuming()