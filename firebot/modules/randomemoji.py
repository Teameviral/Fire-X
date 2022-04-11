"""
Get Random Emoji as Image..
Syntax : `.randomoji`
"""

from firebot import CMD_HELP

import os
from ..utils import admin_cmd, sudo_cmd, edit_or_reply
from multiutility import EmojiCreator

Emoji = EmojiCreator()

@borg.on(admin_cmd(pattern="randomoji", outgoing=True))  # pylint:disable=E0602
@borg.on(sudo_cmd(pattern="randomoji"))
async def _(event):
    mmmm = await edit_or_reply(event, "**Generating Your Random Emoji ⏰✍️**")
    emoji = Emoji.get_random()
    await event.respond("**--- Random Emoji For You ---**", file=emoji)
    os.remove(emoji)
    await mmmm.delete()


CMD_HELP.update({"randomoji":"Get Random Emoji as Image."})
