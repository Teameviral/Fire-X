import asyncio
from collections import deque

from telethon import events

from firebot import CMD_HELP


@fire.on(events.NewMessage(pattern=r"\.rain", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    deq = deque(list("☁️⛈Ř/~\İŇ🌬⚡🌪"))
    for _ in range(100):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


CMD_HELP.update(
    {
        "rain": "**Rain**\
\n\n**Syntax : **`.rain`\
\n**Usage :** Funny plugin that shows rain."
    }
)
