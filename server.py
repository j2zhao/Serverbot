from flask import Flask, request
import json
import requests
import nltk

import bot

app = Flask(__name__)

# This needs to be filled with the Page Access Token that will be provided
# by the Facebook App that will be created.
PAT = 'EAAZAzC3ySp6UBAIPjBI2LZADVDYrYjAFvAnJZAtsM0GWA36gHmKezxc8nZA3NDZAOewP0gjQ0ZBKuN626kZAUAN0s06MZCEoS884VXmDBWoR4nTU7zBWNBWJ0fHJyth9E7BvZAjQZBZAAhzUrjeFXjWuR4niOrflXoCYreDWaxTlt9hhAZDZD'


@app.route('/', methods=['GET'])
def handle_verification():
    print('Handling Verification.')
    if request.args.get('hub.verify_token', '') == 'thechatiscorrect':
        print('Verification successful!')
        return request.args.get('hub.challenge', '')
    else:
        print('Verification failed!')
        return 'Error, wrong validation token'


@app.route('/', methods=['POST'])
def handle_messages():
    print('Handling Messages')
    payload = request.get_data()
    print(payload)
    for sender, message in messaging_events(payload):
        print('Incoming from {}: {}'.format(sender, message))
        send_message(PAT, sender, bot.respond(message))
    return 'ok'


def messaging_events(payload):
    '''Generate tuples of (sender_id, message_text) from the
    provided payload.
    '''
    data = json.loads(payload.decode())
    messaging_events = data['entry'][0]['messaging']
    for event in messaging_events:
        if 'message' in event and 'text' in event['message']:
            yield event['sender']['id'], event['message']['text'].encode('unicode_escape').decode('utf-8')
        else:
            yield event['sender']['id'], 'I can\'t echo this'


def send_message(token, recipient, text):
    '''Send the message text to recipient with id recipient.
    '''
    r = requests.post('https://graph.facebook.com/v2.6/me/messages',
        params={'access_token': token},
        data=json.dumps({
            'recipient': {'id': recipient},
            'message': {'text': text}
        }),
        headers={'Content-type': 'application/json'})
    if r.status_code != requests.codes.ok:
        print(r.text)

if __name__ == '__main__':
    nltk.data.path.append('./nltk_data/')
    app.run()