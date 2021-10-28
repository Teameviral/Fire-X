"""
Insult someone.
Syntax : `.insult`
"""

import os
from firebot import CMD_HELP
from multiutility import MultiClient
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

Client = MultiClient()

@borg.on(admin_cmd(pattern="insult", outgoing=True))  # pylint:disable=E0602
@borg.on(sudo_cmd(pattern="insult"))
async def _(event):
    insult = Client.get_insult()
    await edit_or_reply(event, insult)

 
CMD_HELP.update({"insult":"Get some random insult."})
