'''
Created on 09/11/2012

@author: rwidelka
'''

import pika
import sys

def main(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='logs',
                             type='fanout')
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=msg)
    print " [x] Sent %r" % (msg,)
    connection.close()

if __name__ == '__main__':
    #message = ' '.join(sys.argv[1:]) or "info: Hello World!"
    for message in ['info: Event1', 'info: Event2', 'debug: Event3', 'error: Event5']:
        main(message)
