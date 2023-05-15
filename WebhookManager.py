import requests
import colorama
import json
import ctypes
import time
import os
import rgbprint
from os import system
system("cls")

os.system("cls")
ctypes.windll.kernel32.SetConsoleTitleW("https://github.com/ZxcLexawww")

from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint("▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄▄·  ▄ .▄            ▄ •▄     • ▌ ▄ ·.  ▄▄▄·  ▐ ▄  ▄▄▄·  ▄▄ • ▄▄▄ .▄▄▄  ", color="FF0000")
from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint("██· █▌▐█▀▄.▀·▐█ ▀█▪██▪▐█▪     ▪     █▌▄▌▪    ·██ ▐███▪▐█ ▀█ •█▌▐█▐█ ▀█ ▐█ ▀ ▪▀▄.▀·▀▄ █·", color="B30000")
from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint("██▪▐█▐▐▌▐▀▀▪▄▐█▀▀█▄██▀▐█ ▄█▀▄  ▄█▀▄ ▐▀▀▄·    ▐█ ▌▐▌▐█·▄█▀▀█ ▐█▐▐▌▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄▐▀▀▄ ", color="860000")
from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint("▐█▌██▐█▌▐█▄▄▌██▄▪▐███▌▐▀▐█▌.▐▌▐█▌.▐▌▐█.█▌    ██ ██▌▐█▌▐█ ▪▐▌██▐█▌▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌▐█•█▌", color="660000")
from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint(" ▀▀▀▀ ▀▪ ▀▀▀ ·▀▀▀▀ ▀▀▀ · ▀█▄▀▪ ▀█▄▀▪·▀  ▀    ▀▀  █▪▀▀▀ ▀  ▀ ▀▀ █▪ ▀  ▀ ·▀▀▀▀  ▀▀▀ .▀  ▀", color="400000")

webhookurl = input("Your Webhook Url: ")
webhookname = input("Webhook name: ")
avatar_w = input("Webhook avatar: ")
webhookmessagecontent = input("Message content: ")
message = {"content": webhookmessagecontent, "avatar_url": avatar_w, 'username': webhookname}
message = json.dumps(message)
num_times = int(input("Amount of messages: "))
for i in range(num_times):
    response = requests.post(webhookurl, data=message, headers={"Content-Type": "application/json"})
    if response.status_code == 204:
      from rgbprint import rgbprint 
from rgbprint import Color 
rgbprint("Sended!", color="00F7A9")  

time.sleep(2)
quit()