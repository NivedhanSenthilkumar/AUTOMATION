import json

from botocore.vendored import requests

def lambda_handler(event, context):

    if 'body' in event:
        message_event = json.loads(event['body'])['events'][0]
        reply_token = message_event['replyToken']
        message_text = message_event['message']['text']

        requests.post('https://api.line.me/v2/bot/message/reply',
            data=json.dumps({
                'replyToken': reply_token,
                'messages': [{'type': 'text', 'text': message_text.upper()}]
            }),
            headers={
                # TODO: Put your channel access token in the Authorization header
                'Authorization': HUNZZaa+3sMssHOv88a0NvV/ma2TZqk44UV+yK3SLNwpO6erGuEW1bW1RETIUjFtxjRxiseeJzPYK+XQAthI1esruGudE298W7nwlyJkfnTrKSaYjtjN872Jr4tRrJN6WrCgPZqzLdjF1lnXrg9tqwdB04t89/1O/w1cDnyilFU=,
                'Content-Type': 'application/json'
            }
        )

    return {
        'statusCode': 200
    }