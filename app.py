import os
from telnetlib import Telnet
from time import sleep
import urllib.parse
import requests

TELEGRAM_BOT_KEY = os.environ["TELEGRAM_BOT_KEY"]
TELEGRAM_CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]
SMS_GATEWAY_IP = os.environ["SMS_GATEWAY_IP"]
SMS_GATEWAY_PORT = os.environ["SMS_GATEWAY_PORT"]
SMS_GATEWAY_USERNAME = os.environ["SMS_GATEWAY_USERNAME"]
SMS_GATEWAY_SECRET = os.environ["SMS_GATEWAY_SECRET"]

with Telnet(SMS_GATEWAY_IP, int(SMS_GATEWAY_PORT)) as tn:
    tn.write(f"""Action: login
Username: {SMS_GATEWAY_USERNAME}
Secret: {SMS_GATEWAY_SECRET}


    """.encode('ascii'))
    try:
        tn.read_until(b"Response: Success").decode('ascii')
        print("Connected!")
    except:
        raise Exception('Could not connect')

    while True:
        data = tn.read_very_eager()

        if b"Event: ReceivedSMS" in data:
            data = data.decode('ascii')
            
            lines = data.splitlines()

            sms = {}

            for line in lines:
                if line.startswith('Sender: '):
                    sms['From'] = line.replace('Sender: ', '')

                elif line.startswith('Content: '):
                    sms['Message'] = urllib.parse.unquote(line.replace('Content: ', ''))

            message = f"""From: {sms['From']}

Message: 
{sms['Message']}

To reply:
/send {sms['From'].replace('+', '')}"""
             
            r = requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_KEY}/sendMessage", json={"chat_id": TELEGRAM_CHAT_ID, "text": message})
            print(message)

        sleep(1)