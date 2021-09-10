# SMS2Telegram

## Requirements
 - Yeastar TG100 SMS Gateway with:
    - Active SIM card inserted
    - SMS API enabled and IP whitelisted (refer to their manual)
 - Telegram Bot (you can create one through the [Bot Father](https://t.me/botfather))
 - Docker

## Description
This connects to the SMS Server as a telnet client and listens for inbound SMS on Asterisk. Refer to the `app.py` for more information.

## Get Telegram Chat ID
Say something to your Telegram Bot and visit `https://api.telegram.org/bot<your bot key here>/getUpdates` in our browser and find the chat ID there.

## Run
```bash
git clone https://github.com/koenvaneijk/sms2telegram
cd sms2telegram
docker build -t sms2telegram .
docker run
    -d
    -e TELEGRAM_BOT_KEY=<your telegram bot key> \
    -e TELEGRAM_CHAT_ID=<your telegram chat id> \
    -e SMS_GATEWAY_IP=<gateway ip> \
    -e SMS_GATEWAY_PORT=<port> \
    -e SMS_GATEWAY_USERNAME=<username> \
    -e SMS_GATEWAY_SECRET=<password> \
    sms2telegram
```