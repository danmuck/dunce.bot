import requests
import os
from dotenv import load_dotenv
load_dotenv()

U_TOKEN = os.getenv('U_TOKEN')
BOT_TOKEN = os.getenv('BOT_TOKEN')
# https://discord.com/api/v9/channels/882994482579140742/messages?limit=50



# channel_id = '882994482579140742'

not_spam = '882971968507363359'
python_spam = '881222079356219413' #discussion
spam_ = '881226606490841088'
test_spam = '883778568004456458'


def message_():
    mess_con = input('\nSEND [:] ')
    payload = {'content': f'```{mess_con}```'}
    headers = {'authorization': U_TOKEN}
    channel_ = input('TO [:] ')
    if channel_ == 'not spam':
        channel_id = not_spam
        print(f'\nPOSTAL [:] sending message to #not-spam\n')
        return requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=headers)

    elif channel_ == 'python':
        channel_id = python_spam
        print(f'\nPOSTAL [:] sending message to #discussion\n')
        return requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=headers)

    elif channel_ == 'spam':
        channel_id = spam_
        print(f'\nPOSTAL [:] sending message to #spam\n')
        return requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=headers)

    else:
        channel_id = test_spam
        print(f'\nPOSTAL [:] sending message to #spam-burner\n')
        return requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', data=payload, headers=headers)

if __name__ == '__main__':
    message_()
    
# {content: "sdfsdf", nonce: "888138506361110528", tts: false}
# content: "sdfsdf"
# nonce: "888138506361110528"
# tts: false

