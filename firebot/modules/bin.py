from telethon import events, functions
from telethon.errors.rpcerrorlist import YouBlockedUserError

from firebot import bot as chrisdroid

from ..utils import admin_cmd as chrisdroidboy


@chrisdroid.on(chrisdroidboy(pattern="bin2 ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Searching ur bin 😅😁...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/bin {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Boss! Please Unblock @Carol5_bot ")
            return
        if respond.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@chrisdroid.on(chrisdroidboy(pattern="vbv ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/vbv {}".format(danish))
            respond = await response
        except YouBlockedUserError:
            await event.reply("Boss! Please Unblock @Carol5_bot ")
            return
        if respond.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:

            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@chrisdroid.on(chrisdroidboy(pattern="key ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/key {}".format(danish))
            response = await response
        except YouBlockedUserError:
            await event.reply("Boss! Please Unblock @Carol5_bot ")
            return
        if response.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:
            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()


@chrisdroid.on(chrisdroidboy(pattern="iban2 ?(.*)"))
async def _(event):
    if event.fwd_from:
        return

    danish = event.pattern_match.group(1)
    chat = "@Carol5_bot"
    await event.edit("Connecting...")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1247032902)
            )
            await event.client.send_message(chat, "/iban {}".format(danish))
            response = await response
        except YouBlockedUserError:
            await event.reply("Boss! Please Unblock @Carol5_bot ")
            return
        if response.text.startswith(" "):
            await event.edit("That bot is dead bro now this cmd is useless 😂😂")
        else:
            await event.client.send_message(event.chat_id, respond.message)
    await bot(functions.messages.DeleteHistoryRequest(peer=chat, max_id=0))
    await event.delete()
