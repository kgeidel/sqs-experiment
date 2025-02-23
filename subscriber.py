#!/usr/bin/env python3

######################################################
# MSDS434 - Section 55 - Winter '25
# Module 8: Publisher/Subscriber model demonstration
# 
# Kevin Geidel
# 
# subscriber.py - Fetch messages from AWS SQS queue
######################################################

# Python imports
import time
import os

# 3rd party imports
import boto3

def get_client():
    return boto3.client('sqs')

def get_queue_url():
    queue_name = os.getenv('SQS_QUEUE_NAME')
    return get_client().get_queue_url(QueueName=queue_name).get('QueueUrl')

def main():
    client = get_client()
    queue_url = get_queue_url()
    while True:
        print("\nChecking for messages...", end='')
        response = client.receive_message(
            QueueUrl = queue_url,
            MaxNumberOfMessages = 10,
            WaitTimeSeconds = 4,
        )
        messages = response.get('Messages')
        if messages is None:
            print("NONE!")
        else:
            print(f"received {len(messages)} message(s)!")
            for message in messages:
                print(message.get('Body'))
                response = client.delete_message(
                    QueueUrl=queue_url,
                    ReceiptHandle=message.get('ReceiptHandle'),
                )
        time.sleep(4)
        #break

if __name__ == '__main__':
    main()