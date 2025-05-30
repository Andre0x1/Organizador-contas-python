#!/usr/bin/env python
import pika, sys, os

def main():
    CLOUDAMQP_URL = os.environ.get('')

    params = pika.URLParameters(CLOUDAMQP_URL)
    params.socket_timeout = 5
    connection = pika.BlockingConnection(params)
    channel = connection.channel()


    channel.queue_declare(queue="DadosConta")

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue='DadosConta', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)