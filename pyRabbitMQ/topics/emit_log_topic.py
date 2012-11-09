'''
Created on 09/11/2012

@author: rwidelka
'''

import pika
import sys

def main(routing_key, message):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='topic_logs',
                             type='topic')
    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key,
                          body=message)
    print " [x] Sent %r:%r" % (routing_key, message)
    connection.close()

if __name__ == '__main__':
    #routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
    #message = ' '.join(sys.argv[2:]) or 'Hello World!'
    for routing_key, message in [("kern.critical", "A critical kernel error"), ("cron.critical", "A critical cron error"),
                                 ("kern.info", "A kernel info"), ("cron.info", "A cron info")]:
        main(routing_key, message)