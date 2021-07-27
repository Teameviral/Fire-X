import asyncio
import random
from telethon import events, version
from userbot import ALIVE_NAME, currentversion
from userbot.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins
from firebot import CMD_HELP

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "firebot"

chrissudo = Config.SUDO_USERS

if chrissudo:
    sudou = "True"
else:
    sudou = "False"


edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/f36754b7d29242bd7b15c.jpg"
file2 = "https://telegra.ph/file/9c135ed934dd65bff97ac.jpg"
file3 = "https://telegra.ph/file/9ab1513be4a75fa59dd12.jpg"
file4 = "https://telegra.ph/file/9ab1513be4a75fa59dd12.jpg"
""" =======================CONSTANTS====================== """



pm_caption = "  __**★ғɪʀᴇ-x ɪs ʀᴜɴɴɪɴɢ sᴜᴄᴇssғᴜʟʟʏ★**__\n\n"

pm_caption += f"**━━━━━━━|━━━━━|━━━━━━**\n\n"
pm_caption += (
    f"                 ◉✿ ᴍᴀsᴛᴇʀ ✿◉\n  **{DEFAULTUSER}**\n\n"
)
pm_caption += f"┏━━━━━━━ɪɴғᴏ━━━━━━━━\n"
pm_caption += f"┣•➳➠ `ᴛᴇʟᴇᴛʜᴏɴ:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `ᴠᴇʀsɪᴏɴ:` `{currentversion}`\n"
pm_caption += f"┣•➳➠ `ᴜᴘᴛɪᴍᴇ:` `{uptime}`\n"
pm_caption += f"┣•➳➠ `ᴄʜᴀɴɴᴇʟ:` [ᴊᴏɪɴ](https://t.me/Fire_X_CHANNEL)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f" ||•|| sᴇᴄᴜʀɪᴛʏ ʙʏ ғɪʀᴇ-x ||•||\n"
pm_caption += " [ɢɪᴛʜᴜʙ](https://github.com/Chrisdroid1/Fire-X) • [ɢʀᴏᴜᴘ](https://t.me/FireXUserBot)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    await alive.delete()
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file3)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file1)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file4)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file1)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(alive.chat_id, ok7, file=file2) 

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(alive.chat_id, ok8, file=file3)

    await asyncio.sleep(edit_time)
    ok10 = await borg.edit_message(alive.chat_id, ok9, file=file1)
    
    await asyncio.sleep(edit_time)
    ok11 = await borg.edit_message(alive.chat_id, ok10, file=file3)
    
    await asyncio.sleep(edit_time)
    ok12 = await borg.edit_message(alive.chat_id, ok11, file=file2)
    
    await asyncio.sleep(edit_time)
    ok13 = await borg.edit_message(alive.chat_id, ok12, file=file4)
    
    await asyncio.sleep(edit_time)
    ok14 = await borg.edit_message(alive.chat_id, on, file=file1)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if Fire-X UserBot is Alive"
    }
)
