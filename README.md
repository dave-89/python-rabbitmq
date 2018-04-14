# python-rabbitmq

Simple demo for rabbitMQ using the python library *pika*.
Apart from the message broker, this demo is made by three components:
- client: it creates one message per second and it writes on the first queue (*serverQueue*)
- server: it consumes *serverQueue* and process the messages (at a rate of 0.5 messages per second) and published the result on a second queue (*dispatcherQueue*)
- dispatcher: it consumes *dispatcherQueue*