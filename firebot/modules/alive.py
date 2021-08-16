"""Check if firebot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from telethon import version
from uniborg.util import fire_on_cmd, sudo_cmd

from firebot import ALIVE_NAME, CMD_HELP, Lastupdate
from firebot.Configs import Config
from firebot.modules import currentversion


# Functions
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


uptime = get_readable_time((time.time() - Lastupdate))
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "firebot"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "  __**★ғɪʀᴇ-x ɪs ʀᴜɴɴɪɴɢ sᴜᴄᴇssғᴜʟʟʏ★**__\n\n"

pm_caption += f"**━━━━━━━|━━━━━|━━━━━━**\n\n"
pm_caption += f"                 ◉✿ ᴍᴀsᴛᴇʀ ✿◉\n  **{DEFAULTUSER}**\n\n"
pm_caption += f"┏━━━━━━━ɪɴғᴏ━━━━━━━━\n"
pm_caption += f"┣•➳➠ `ᴛᴇʟᴇᴛʜᴏɴ:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `ᴠᴇʀsɪᴏɴ:` `{currentversion}`\n"
pm_caption += f"┣•➳➠ `ᴜᴘᴛɪᴍᴇ:` `{uptime}`\n"
pm_caption += f"┣•➳➠ `ᴄʜᴀɴɴᴇʟ:` [ᴊᴏɪɴ](https://t.me/Fire_X_CHANNEL)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f" ||•|| sᴇᴄᴜʀɪᴛʏ ʙʏ ғɪʀᴇ-x ||•||\n"
pm_caption += " [ɢɪᴛʜᴜʙ](https://github.com/TeamEviral/Fire-X) • [ɢʀᴏᴜᴘ](https://t.me/FireXUserBot)"


@fire.on(fire_on_cmd(pattern=r"alive"))
@fire.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def chris(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if firebot UserBot is Alive"
    }
)
