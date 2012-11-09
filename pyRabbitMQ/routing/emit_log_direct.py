'''
Created on 09/11/2012

@author: rwidelka
'''

import pika
import sys

def main(severity, msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='direct_logs',
                             type='direct')
    channel.basic_publish(exchange='direct_logs',
                          routing_key=severity,
                          body=msg)
    print " [x] Sent %r:%r" % (severity, msg)
    connection.close()

if __name__ == '__main__':
    #severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
    #message = ' '.join(sys.argv[2:]) or 'Hello World!'
    for severity, message in [('error', 'Error1'), ('error', 'Error2'), ('warning', 'Warning1'), ('info', 'Info1'), ('error', 'Error3')]:
        main(severity, message)