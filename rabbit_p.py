import pika
import time
from functions import entln_package_creator


def publish_message(channel):
    """
    message passed to "logs" exchange, routing_key is name of the queue but here it is empty because
    name will be given randomly due to every time we start to get a fresh and empty queue. body is message
    """
    while True:
        message = entln_package_creator()
        channel.basic_publish(exchange='logs',
                              routing_key='',
                              body=message)
        print(" [x] Sent %r" % message)
        time.sleep(5)


def  make_connection_and_publish():
    # Make connection with rabbitmq
        connection = pika.BlockingConnection(pika.ConnectionParameters(
                port=32778,host='localhost'))
        channel = connection.channel()

        # Declearing an exchange with name "logs" and type of "fanout", this exchange will seperate and deliver the message
        channel.exchange_declare(exchange='logs',
                                 type='fanout')

        publish_message(channel)
        connection.close()


def connect():
    try:
        make_connection_and_publish()
    except Exception as e:
        print "Connection problem occured"
        print e
        return False


def main():
    result = connect()
    if not result:
        while True:
            time.sleep(5)
            connect()


if __name__ == '__main__':
    main()
