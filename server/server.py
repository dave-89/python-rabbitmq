import pika
import json
import time

print('Opening connection...')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

incomingQueue = 'serverQueue'
outgoingQueue = 'dispatcherQueue'

print('Connecting to queues...')
channel.queue_declare(queue=incomingQueue)
channel.queue_declare(queue=outgoingQueue)


def publish_results(result):
    print('Publishing result on outgoing queue: {}...'.format(outgoingQueue))
    channel.basic_publish(exchange='',
                          routing_key=outgoingQueue,
                          body=json.dumps({
                              "result": result
                          })
                          )
    print('Message published')


def process_data(ch, method, properties, body):
    message = json.loads(body.decode())
    print("Received message: {}".format(message))
    print("Performing very long operation...")
    time.sleep(2)
    print("Operation completed")
    x = message['x']
    result = x*x
    print("Result: {}".format(result))
    publish_results(result  )


channel.basic_consume(consumer_callback=process_data,
                      queue=incomingQueue,
                      no_ack=True)

print('Listening for messages (process time .5 messages per second)...')
channel.start_consuming()
