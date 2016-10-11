import pika
import time

def callback(ch, method, properties, body):
    print(" [x] received by c1 %r" % body)


def  make_connection_and_listen():
    # Make connection with rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(
            port=32778,host='localhost'))
    channel = connection.channel()

    # Decleare an exchange to receive messages from it
    channel.exchange_declare(exchange='logs',
                             type='fanout')

    # Decleare a queue name to receive message according to that queue name, and make it random name so that every time
    # get an empty queue
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    # Bind the queue and exchange, here "logs" is exchange name
    channel.queue_bind(exchange='logs',
                       queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)


def connect():
    try:
        make_connection_and_listen()
    except Exception as e:
        while True:
            print "Connection problem occured "
            return False


def main():
    result = connect()
    if not result:
        while True:
            time.sleep(5)
            connect()


if __name__ == '__main__':
    main()
