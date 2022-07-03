import credentials
import requests
import json

def send_message(message):
    headers = {
        'Authorization': 'Bearer ' + get_token(),
    }

    json_data = {
        'messaging_product': 'whatsapp',
        'to': '+33768281173',
        'type': 'template',
        'template': {
            'name': 'hello_world',
            'language': {
                'code': 'en_US',
            },
        },
    }

    response = requests.post('https://graph.facebook.com/v12.0/FROM_PHONE_NUMBER_ID/messages', headers=headers, json=json_data)

    print(response.text)

def get_token():
    params = {
        'client_id': credentials.CLIENT_ID,
        'client_secret': credentials.CLIENT_SECRET,
        'grant_type': 'client_credentials',
    }

    response = requests.get('https://graph.facebook.com/oauth/access_token', params=params)
    print(response.text)
    print()
    
get_token()