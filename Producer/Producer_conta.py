import pika
import os


def produceMessage(message):
    CLOUDAMQP_URL = os.environ.get('')
    params = pika.URLParameters(CLOUDAMQP_URL)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()
    channel.queue_declare(queue="DadosConta")
    message_body = message
    channel.basic_publish(exchange='', routing_key='DadosConta', body=message_body)
    print(f" [x] Sent '{message_body}' to queue '{'DadosConta'}'")
    connection.close()


produceMessage("Conta cemig")


