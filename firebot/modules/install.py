import asyncio
import os
from pathlib import Path

from firebot import CMD_HELP
from firebot.function import get_all_modules
from firebot.utils import fire_on_cmd, load_module

DELETE_TIMEOUT = 5


@fire.on(fire_on_cmd(pattern="install"))
async def install(event):
    if event.fwd_from:
        return
    if event.reply_to_msg_id:
        sedplugin = await event.get_reply_message()
        try:
            downloaded_file_name = await event.client.download_media(
                sedplugin,
                "firebot/modules/",
            )
            if "(" not in downloaded_file_name:
                path1 = Path(downloaded_file_name)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                await event.edit(
                    "Fire-X Installed `{}` Sucessfully.".format(
                        os.path.basename(downloaded_file_name)
                    )
                )
            else:
                os.remove(downloaded_file_name)
                await event.edit(
                    "Errors! This plugin is already installed/pre-installed."
                )
        except Exception as e:  # pylint:disable=C0103,W0703
            await event.edit(
                f"Error While Installing This Plugin, Please Make Sure That its py Extension. \n**ERROR :** {e}"
            )
            os.remove(downloaded_file_name)
    await asyncio.sleep(DELETE_TIMEOUT)
    await event.delete()


@borg.on(fire_on_cmd(pattern="pl ?(.*)"))
async def _(event):
    lul = event.pattern_match.group(1)
    yesm, nope, total_p = await get_all_modules(event, borg, lul)
    await event.edit(
        f"Installed {yesm} PLugins. Failed To Install {nope} Plugins And There Were Total {total_p} Plugins"
    )


CMD_HELP.update(
    {
        "install": "**Install**\
\n\n**Syntax : **`.install <reply to plugin>`\
\n**Usage :** it installs replyed plugin"
    }
)
