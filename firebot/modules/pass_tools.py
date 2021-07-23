import secrets
from random import *

from password_strength import PasswordStats
from uniborg.util import fire_on_cmd

from firebot import CMD_HELP
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="passcheck (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stats = PasswordStats(input_str)
    sedbruh = stats.strength()
    if stats.strength() >= 0.2:
        await event.edit(
            f"<b><u>Password Checked</b></u> \n<b>Password :</b> <code>{input_str}</code> \n<b>Strength :</b> <code>{sedbruh}</code> \n<b>Result :</b> <code>Good Password</code>",
            parse_mode="HTML",
        )
    else:
        await event.edit(
            f"<b><u>Password Checked</b></u> \n<b>Password :</b> <code>{input_str}</code> \n<b>Strength :</b> <code>{sedbruh}</code> \n<b>Result :</b> <code>Bad Password</code>",
            parse_mode="HTML",
        )


@fire.on(fire_on_cmd(pattern=r"passgen"))
async def hi(event):
    if event.fwd_from:
        return
    okbabe = secrets.token_urlsafe(16)
    stats = PasswordStats(okbabe)
    sedbruh = stats.strength()
    await event.edit(
        f"<b>Password</b> : <code>{okbabe}</code> \n<b>Strength :</b> <code>{sedbruh}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "password_tools": "**Password Tools**\
\n\n**Syntax : **`.passgen`\
\n**Usage :** This plugin generates good strong password for you.\
\n\n**Syntax : **`.passcheck <your password>`\
\n**Usage :** This plugin checks the strength of your password."
    }
)
