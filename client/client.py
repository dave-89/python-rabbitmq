import pika
import json
import time

print('Opening connection...')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

serverQueue = 'serverQueue'

print('Creating queue...')
channel.queue_declare(queue=serverQueue)

print('Sending 10 messages at one message per second...')
i = 0
while i < 10:
    time.sleep(1)
    message = {
        "x": i
    }
    channel.basic_publish(exchange='',
                          routing_key=serverQueue,
                          body=json.dumps(message)
                          )
    print('Message {} sent'.format(i))
    i += 1

print('Closing connection...')
connection.close()
print('Connection closed')
