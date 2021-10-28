"""
Insult someone.
Syntax : `.insult`
"""

import os
from userbot.cmdhelp import CmdHelp
from multiutility import MultiClient
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

Client = MultiClient()

@borg.on(admin_cmd(pattern="insult", outgoing=True))  # pylint:disable=E0602
@borg.on(sudo_cmd(pattern="insult"))
async def _(event):
    insult = Client.get_insult()
    await edit_or_reply(event, insult)

 
CmdHelp("insult").add_command(
  "insult", None, "Get some random insult."
).add()
