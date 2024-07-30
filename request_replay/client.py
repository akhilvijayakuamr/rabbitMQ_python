import pika
import uuid

def on_reply_message_recived(ch, method, properties, body):
    print(f'replay is recived by {body}')

connection_parameters =  pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

replay_queue = channel.queue_declare(queue='', exclusive=True)

channel.basic_consume(queue=replay_queue.method.queue, auto_ack=True, 
                      on_message_callback=on_reply_message_recived)

channel.queue_declare('request_queue')

message = "can i request a replay ?"

corr_id = str(uuid.uuid4())

print(f'sending request: {corr_id}')

channel.basic_publish(exchange='', routing_key='request-queue',properties=pika.BasicProperties(
        reply_to=replay_queue.method.queue,
        correlation_id=corr_id,
    ), body=message)

print(f"starting client: {message}")

channel.start_consuming()