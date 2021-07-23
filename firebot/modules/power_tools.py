import os
import sys

from firebot import CMD_HELP
from firebot.utils import fire_on_cmd


@fire.on(fire_on_cmd("restart"))
async def _(event):
    if event.fwd_from:
        return
    # await asyncio.sleep(2)
    # await event.edit("Restarting [██░] ...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    # await event.edit("Restarting [███]...\n`.ping` me or `.help` to check if I am online after a lil bit.")
    # await asyncio.sleep(2)
    await event.edit("Restarted. `.ping` me or `.help` me to check if I am online")
    await borg.disconnect()
    # https://archive.is/im3rt
    os.execl(sys.executable, sys.executable, *sys.argv)
    # You probably don't need it but whatever
    quit()


@fire.on(fire_on_cmd("shutdown"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Turning off ...Manually turn me on later")
    await borg.disconnect()


CMD_HELP.update(
    {
        "power_tools": "**Power Tools**\
\n\n**Syntax : **`.restart`\
\n**Usage :** restarts your  Fire-X.\
\n\n**Syntax : **`.shutdown`\
\n**Usage :** Shuts down your Fire-X."
    }
)
