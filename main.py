print('Hello world ')
print('Welcome to my source ')



from telethon.sync import TelegramClient
from telethon.sessions import StringSession
print("******************************************")
APP_ID = int(input("ENTER 𝙰𝙿𝙿 𝙸𝙳 ➺ > "))
API_HASH = input("- ENTER 𝙰𝙿𝙸 𝙷𝙰𝚂𝙷 ➺ > ")
print("\n--------------------------")

with TelegramClient(StringSession(), APP_ID, API_HASH) as tb:
    print("")
    print("\n---------------------------")
    print("")
    print("You Will get STRING SESSION  in save msg")
    jmth = tb.send_message("me", f"`{tb.session.save()}`")
    jmth.reply( '-هذا كود تيرمكس عَيني.

𝗗𝗘𝗩 : @AbdSha1 - @EnYusuf ')
