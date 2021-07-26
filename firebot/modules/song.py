import asyncio

from telethon.errors.rpcerrorlist import YouBlockedUserError

from firebot import CMD_HELP, bot
from firebot.utils import fire_on_cmd


@fire.on(fire_on_cmd(pattern="netease ?(.*)"))
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Getting Your Music```")
    async with bot.conversation(chat) as conv:
        await asyncio.sleep(2)
        await netase.edit("`Downloading...Please wait`")
        try:
            msg = await conv.send_message(link)
            response = await conv.get_response()
            respond = await conv.get_response()
            """ - don't spam notif - """
            await bot.send_read_acknowledge(conv.chat_id)
        except YouBlockedUserError:
            await netase.reply("```Please unblock @WooMaiBot and try again```")
            return
        await netase.edit("`Sending Your Music...`")
        await asyncio.sleep(3)
        await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id, [msg.id, response.id, respond.id])
    await netase.delete()


CMD_HELP.update(
    {
        "song": "**Song**\
\n\n**Syntax : **`.netease <song name>`\
\n**Usage :** downloads the song from internet and uploades it."
    }
)
