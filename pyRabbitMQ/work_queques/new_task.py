'''
Created on 09/11/2012

@author: rwidelka
'''
import pika
import sys

def main(msg):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue', durable=True)
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=msg,
                          properties=pika.BasicProperties(
                              delivery_mode =2, # make message persistent
                          ))
    print " [x] Sent %r" % (message,)
    connection.close()
    
if __name__ == '__main__':
    #message = ' '.join(sys.argv[1:]) or "Hello World!"
    for message in ['First message.', 'Second message..', 'Third message...', 'Fourth message....', 'Fifth message.....']:
        main(message)