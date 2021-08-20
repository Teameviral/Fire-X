from var import Var
from firebot.Configs import Config
from firebot.utils import fire_on_cmd


@borg.on(fire_on_cmd(pattern="frwd"))
async def _(event):
    if event.fwd_from:
        return
    if Var.PLUGIN_CHANNEL is None:
        await event.edit(
            "Please set the required environment variable `PLUGIN_CHANNEL` for this plugin to work"
        )
        return
    try:
        e = await borg.get_entity(Var.PLUGIN_CHANNEL)
    except Exception as e:
        await event.edit(str(e))
    else:
        re_message = await event.get_reply_message()
        # https://t.me/telethonofftopic/78166
        fwd_message = await borg.forward_messages(e, re_message, silent=True)
        await borg.forward_messages(event.chat_id, fwd_message)
        await fwd_message.delete()
        await event.delete()
