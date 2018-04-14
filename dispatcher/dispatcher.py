import pika
import json

print('Opening connection...')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

incomingQueue = 'dispatcherQueue'

print('Connecting to queues...')
channel.queue_declare(queue=incomingQueue)


def process_data(ch, method, properties, body):
    message = json.loads(body.decode())
    print('Received message: {}'.format(message))
    print("Cool. I'm gonna do something amazing with it :)")


channel.basic_consume(consumer_callback=process_data,
                      queue=incomingQueue,
                      no_ack=True)


print('Listening to the queue {}'.format(incomingQueue))
channel.start_consuming()
