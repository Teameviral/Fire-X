from telethon.sessions import StringSession
from telethon.sync import TelegramClient

ok = """ ____  ____  __  ____   __   _  _
(  __)(  _ \(  )(    \ / o\ ( \/ )
 ) _)  )   / )(  ) D (/    \ )  /
(__)  (__\_)(__)(____/\_/\_/(__/
"""
print(ok)
APP_ID = int(input("Enter APP ID here: \n"))
API_HASH = input("Enter API HASH here: \n")

with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
    try:
        session = client.session.save()
        client.send_message("me", f"String Session \nTap To Copy. \n`{session}`")
        print("String Generated Sucessfully Check Your Saved Message.")
    except Exception as sed:
        print(f"Something Went Wrong While Generating String \nError : {sed}")
