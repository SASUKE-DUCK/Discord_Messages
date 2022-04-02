# -*- coding: utf-8 -*-
# Module: Discord_Messages
# Created on: 02-04-2022
# Authors: -∞WKS∞-
# Version: 1.5.0

import requests
import random
import logging
logging.basicConfig(level=logging.DEBUG)

# token = 'xxxxxx'
# channel_id = xxxxxx
 
def sendMessage(token, channel_id, message):
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(channel_id)
    data = {"content": message}
    header = {"authorization": token}
 
    r = requests.post(url, data=data, headers=header)
    print(r.status_code)

messages = ['uwu', 'owo', '(///./w/.///)']

for i in range(10):
    sendMessage('token', channel_id, random.choice(messages))