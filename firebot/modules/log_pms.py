import asyncio

from uniborg.util import fire_on_cmd

NO_PM_LOG_USERS = []


@fire.on(fire_on_cmd(incoming=True, func=lambda e: e.is_private))
async def monito_p_m_s(event):
    sender = await event.get_sender()
    if Config.NC_LOG_P_M_S and not sender.bot:
        chat = await event.get_chat()
        if chat.id not in NO_PM_LOG_USERS and chat.id != borg.uid:
            try:
                e = await borg.get_entity(int(Config.PM_LOGGR_BOT_API_ID))
                fwd_message = await borg.forward_messages(e, event.message, silent=True)
            except Exception as e:
                logger.warn(str(e))


@fire.on(fire_on_cmd(pattern="nolog ?(.*)"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    event.pattern_match.group(1)
    chat = await event.get_chat()
    if Config.NC_LOG_P_M_S:
        if event.is_private:
            if chat.id not in borg.storage.NO_PM_LOG_USERS:
                NO_PM_LOG_USERS.append(chat.id)
                await event.edit("Won't Log Messages from this chat")
                await asyncio.sleep(3)
                await event.delete()
