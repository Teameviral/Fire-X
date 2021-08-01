import os

import requests

from firebot import CMD_HELP
from firebot.utils import fire_on_cmd, sudo_cmd


# hmm
@fire.on(fire_on_cmd(pattern="picgen"))
@fire.on(sudo_cmd(pattern="picgen", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return

    url = "https://thispersondoesnotexist.com/image"
    response = requests.get(url)
    if response.status_code == 200:
        with open("JUSTFIRE.jpg", "wb") as f:
            f.write(response.content)

    captin = f"Fake Image By FIRE-X.\nGet Your Own Superpowers From [Fire-X](github.com/FireXbot/Fire-X)."
    fole = "JUSTFIRE.jpg"
    await borg.send_file(event.chat_id, fole, caption=captin)
    await event.delete()
    os.system("rm /root/firebot/JUSTFIRE.jpg ")


CMD_HELP.update(
    {
        "picgen": "**Fake Picture Gen**\
\n\n**Syntax : **`.picgen`\
\n**Usage :** Genetates Fake Image.\
\n\n**Note : **The Person In Picture Really Doesn't Exist."
    }
)
