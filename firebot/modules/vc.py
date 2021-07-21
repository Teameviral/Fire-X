from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc

from firebot.events import register


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@register(outgoing=True, pattern=r"^\.joinvc (.*)")
async def _(event):
    try:
        await event.client(startvc(await get_call(event)))
        await event.edit(event, "`Voice Chat Started...`")
    except Exception as ex:
        await event.edit(event, f"`{str(ex)}`")


@register(outgoing=True, pattern=r"^\.stopvc (.*)")
async def _(event):
    try:
        await event.client(stopvc(await get_call(event)))
        await event.edit(event, "`Voice Chat Stopped...`")
    except Exception as ex:
        await event.edit(event, f"`{str(ex)}`")
