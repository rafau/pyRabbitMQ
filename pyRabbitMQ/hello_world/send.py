'''
Created on 09/11/2012

@author: rwidelka
'''
import pika

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='hello')
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body='Hello World!')
    print " [x] Sent 'Hello World!'"
    connection.close()
    
if __name__ == '__main__':
    main()