print('Hello world ')
print('welcome to my source ')



from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("******************************************")
APP_ID = int(input("ENTER APP ID > "))
API_HASH = input("- ENTER API HASH > ")
print("\n--------------------------")

with TelegramClient(StringSession(), APP_ID, API_HASH) as tb:
    print("")
    print("\n---------------------------")
    print("")
    print("You Will get STRING SESSION  in save msg")
    jmth = tb.send_message("me", f"`{tb.session.save()}`")
    jmth.reply('This is your cod termux by @EnYusuf')