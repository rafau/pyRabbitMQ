'''
Created on 09/11/2012

@author: rwidelka
'''
import pika
import sys


def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)

def main(severities):
    if not severities:
        print >> sys.stderr, "Usage: %s [info] [warning] [error]" % (sys.argv[0],)
        sys.exit(1)

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',
                             type='direct')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    
    for severity in severities:
        channel.queue_bind(exchange='direct_logs',
                           queue=queue_name,
                           routing_key=severity)
    print ' [*] Waiting for logs. To exit press CTRL+C'
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)
    channel.start_consuming()


if __name__ == '__main__':
    severities = sys.argv[1:]
    main(severities)