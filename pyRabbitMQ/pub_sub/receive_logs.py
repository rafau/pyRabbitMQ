'''
Created on 09/11/2012

@author: rwidelka
'''
import pika

def callback(ch, method, properties, body):
    print " [x] %r" % (body,)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs',
                             type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(exchange='logs',
                       queue=queue_name)
    print ' [*] Waiting for logs. To exit press CTRL+C'
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()

if __name__ == '__main__':
    main()