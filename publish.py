#!/usr/bin/env python3

######################################################
# MSDS434 - Section 55 - Winter '25
# Module 8: Publisher/Subscriber model demonstration
# 
# Kevin Geidel
# 
# publish.py - Send messages to the AWS SQS queue
######################################################

# Python imports
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
        message = input("\n\nEnter message to send: ")
        response = client.send_message(
            QueueUrl = queue_url,
            MessageBody = message,
        )
        print(response)

if __name__ == '__main__':
    main()