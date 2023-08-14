import os
import http.client
import json
import random
from urllib.parse import urlparse
import urllib.request

def get_random_line_from_web_file(url):
    with urllib.request.urlopen(url) as response:
        lines = response.read().decode().splitlines()
    return random.choice(lines)

def lambda_handler(event, context):
    # Get Webhook and text file URLs from environment variables
    webhook_url = os.environ['WEBHOOK_URL']
    text_file_url = os.environ['TEXT_FILE_URL']
    
    # Fetch a random line from the text file
    random_line = get_random_line_from_web_file(text_file_url)

    # Set up the HTTP connection for the webhook
    parsed_url = urlparse(webhook_url)
    hostname = parsed_url.netloc
    path = parsed_url.path

    payload = json.dumps({'content': random_line})

    headers = {
        'Content-Type': 'application/json',
        'Content-Length': str(len(payload))
    }

    conn = http.client.HTTPSConnection(hostname)
    conn.request('POST', path, body=payload, headers=headers)
    response = conn.getresponse()

    if response.status == 200 or response.status == 204:
        print('Message sent successfully.')
    else:
        print('Failed to send message.')

    return {
        'statusCode': response.status,
        'body': 'Message sent.'
    }
