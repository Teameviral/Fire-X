import asyncio

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from firebot import CMD_HELP
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern=r"purl ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to any document.**")
        return
    reply_message = await event.get_reply_message()
    chat = "@FileToLinkDXBot"
    reply_message.sender
    await event.edit("**Making public url...\n Powered by @VirtualUserbot**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=1377765808)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @FileToLinkDXBot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@fire.on(admin_cmd(pattern=r"reader ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("**Reply to a URL.**")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("**Reply to a url message.**")
        return
    chat = "@chotamreaderbot"
    reply_message.sender
    await event.edit("**Making instant view...\n Powered by @VirtualUserbot**")
    async with event.client.conversation(chat) as conv:
        try:
            response = conv.wait_event(
                events.NewMessage(incoming=True, from_users=272572121)
            )
            await event.client.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("Please unblock me @chotamreaderbot")
            return
        await event.delete()
        await event.client.send_message(
            event.chat_id, response.message, reply_to=reply_message
        )


@fire.on(admin_cmd(pattern=r"connector ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if event.is_private:
        return
    chat_id = event.chat_id
    await event.client.send_message("missrose_bot", "/connect {}".format(chat_id))
    await event.edit("[Connected](https://t.me/missrose_bot)")
    await asyncio.sleep(3)
    await event.delete()


CMD_HELP.update(
    {
        "exclusive": "**Exclusive**\
\n**Syntax : **`.purl`\
\n**Usage :** Get Public link of any file**\
\n\n**Syntax : **`.reader`\
\n**Usage :** Read any website with telegrams Instant view**\
\n\n**Syntax : **`.connector`\
\n**Usage :** Connect to the chat with Rose**"
    }
)
