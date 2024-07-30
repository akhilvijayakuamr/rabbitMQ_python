import pika
import random
import time


def comp_recive(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f"The message is consumed {body} in processing {processing_time}")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("finish proccesing message")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='cletter')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='cletter', on_message_callback=comp_recive)

channel.start_consuming()