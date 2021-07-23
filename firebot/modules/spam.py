import asyncio
import base64
import os

from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from firebot import CMD_HELP
from firebot.utils import admin_cmd, sudo_cmd, edit_or_reply
from firebot.Configs import Config

LOGGER = Config.PLUGIN_CHANNEL
SUDO_WALA = Config.SUDO_USERS

@bot.on(admin_cmd(pattern="spam (.*)"))
@bot.on(sudo_cmd(pattern="spam (.*)", allow_sudo=True))
async def spammer(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[6:8])
        spam_message = str(e.text[8:])
        await asyncio.wait([e.respond(spam_message) for i in range(counter)])
        await e.delete()
        if LOGGER:
            await e.client.send_message(
                LOGGER_GROUP, "#SPAM \n\n" "Spam was executed successfully"
            )


@bot.on(admin_cmd(pattern="bigspam"))
@bot.on(sudo_cmd(pattern="bigspam", allow_sudo=True))
async def bigspam(fire):
    if not fire.text[0].isalpha() and fire.text[0] not in ("/", "#", "@", "!"):
        fire_msg = fire.text
        firebot_count = int(fire_msg[9:13])
        fire_spam = str(fire.text[13:])
        for i in range(1, firebot_count):
            await fire.respond(fire_spam)
        await fire.delete()
        if LOGGER:
            await fire.client.send_message(
                LOGGER_GROUP, "#BIGSPAM \n\n" "Bigspam was executed successfully"
            )


@bot.on(admin_cmd("dspam (.*)"))
@bot.on(sudo_cmd(pattern="dspam (.*)", allow_sudo=True))
async def spammer(e):
    if e.fwd_from:
        return
    input_str = "".join(e.text.split(maxsplit=1)[1:])
    spamDelay = float(input_str.split(" ", 2)[0])
    counter = int(input_str.split(" ", 2)[1])
    spam_message = str(input_str.split(" ", 2)[2])
    await e.delete()
    for _ in range(counter):
        await e.respond(spam_message)
        await asyncio.sleep(spamDelay)

#@register(outgoing=True, pattern="^.mspam (.*)")
@bot.on(admin_cmd(pattern="mspam (.*)"))
@bot.on(sudo_cmd(pattern="mspam (.*)", allow_sudo=True))
async def tiny_pic_spam(e):
    sender = await e.get_sender()
    me = await e.client.get_me()
    if not sender.id == me.id and not FULL_SUDO:
        return await e.reply("`Sorry sudo users cant access this command..`")
    try:
        await e.delete()
    except:
        pass
    try:
        counter = int(e.pattern_match.group(1).split(" ", 1)[0])
        reply_message = await e.get_reply_message()
        if (
            not reply_message
            or not e.reply_to_msg_id
            or not reply_message.media
            or not reply_message.media
        ):
            return await e.edit("```Reply to a pic/sticker/gif/video message```")
        message = reply_message.media
        for i in range(1, counter):
            await e.client.send_file(e.chat_id, message)
    except:
        return await e.reply(
            f"**Error**\nUsage `!mspam <count> reply to a sticker/gif/photo/video`"
        )


CMD_HELP.update(

    {

        "Spam": "**SPAM**\
\n\n**Syntax : **`.spam <number> <text>`\
\n**Usage :** Sends the text 'X' number of times.\
\n\n**Syntax : **`.mspam <reply to media> <number>`\
\n**Usage :** Sends the replied media (gif/ video/ sticker/ pic) 'X' number of times.\
\n\n**Syntax : **`.dspam <delay> <spam count> <text>`\
\n**Usage :**  Sends the text 'X' number of times in 'Y' seconds of delay\
\n\n**Syntax : **`.bigspam <delay> <spam count> <text>`\
\n**Usage :** Sends the text 'X' number of times. This what firebot is known for. The Best BigSpam Ever."
    }
)
