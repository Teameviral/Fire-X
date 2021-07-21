# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
from uniborg.util import fire_on_cmd

from firebot import CMD_HELP


@fire.on(fire_on_cmd(pattern="tagall"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tagall"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, 100):
        mentions += f"[\u2063](tg://user?id={x.id})"
    await event.reply(mentions)
    await event.delete()


CMD_HELP.update(
    {
        "tagall": "**Tagall**\
\n\n**Syntax : **`.tagall`\
\n**Usage :** tag everyone in a group"
    }
)
