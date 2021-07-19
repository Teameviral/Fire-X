"""Check if Fire-X alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
# CREDITS: @WhySooSerious, @Sur_vivor
import time

from uniborg.util import friday_on_cmd, sudo_cmd

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
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "VirtualUserbot"
PM_IMG = Config.ALIVE_IMAGE
pm_caption = "  __**🔥🔥𝐌𝐀𝐅𝐈𝐀 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄🔥🔥**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 👑𝐌𝐀𝐒𝐓𝐄𝐑👑\n  **『😈[{DEFAULTUSER}](tg://user?id={mafia})😈』**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `Telethon:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `Version:` `{mafiaversion}`\n"
pm_caption += f"┣•➳➠ `Sudo:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `Channel:` [ᴊᴏɪɴ](https://t.me/MafiaBot_Support)\n"
pm_caption += f"┣•➳➠ `Creator:` [Himanshu](https://t.me/H1M4N5HU0P)\n"
pm_caption += f"┣•➳➠ `Supporter:` [HellBoy](https://t.me/kraken_the_badass)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [🔥REPO🔥](https://github.com/MafiaBotOP/MafiaBot) 🔹 [📜License📜](https://github.com/MafiaBotOP/MafiaBot/blob/main/LICENSE)"


@friday.on(friday_on_cmd(pattern=r"alive"))
@friday.on(sudo_cmd(pattern=r"alive", allow_sudo=True))
async def friday(alive):
    await alive.get_chat()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CMD_HELP.update(
    {
        "alive": "**ALive**\
\n\n**Syntax : **`.alive`\
\n**Usage :** Check if UserBot is Alive"
    }
)
