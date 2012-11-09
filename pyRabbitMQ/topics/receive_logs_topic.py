'''
Created on 09/11/2012

@author: rwidelka
'''

import pika
import sys

def callback(ch, method, properties, body):
    print " [x] %r:%r" % (method.routing_key, body,)


def main(binding_keys):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs',
                             type='topic')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue
    
    if not binding_keys:
        print >> sys.stderr, "Usage: %s [binding_key]..." % (sys.argv[0],)
        sys.exit(1)
    for binding_key in binding_keys:
        channel.queue_bind(exchange='topic_logs',
                           queue=queue_name,
                           routing_key=binding_key)
    print ' [*] Waiting for logs. To exit press CTRL+C'
    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    binding_keys = sys.argv[1:]
    main(binding_keys)