"""Evaluate Python Code inside Telegram
Syntax: .eval PythonCode"""
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import io
import sys
import traceback
import time
import asyncio

from uniborg.util import edit_or_reply, fire_on_cmd, sudo_cmd

from firebot import CMD_HELP

EVAL == os.environ.get("EVAL", None)
from . import *

@fire.on(fire_on_cmd("eval"))
async def _(event):
if EVAL == "ON":
        if event.fwd_from:
            return
        cmd = "".join(event.text.split(maxsplit=1)[1:])
        if not cmd:
            return await eor(event, "`What should i run ?..`")
        eviralevent = await eor(event, "`Running ...`")
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None
        try:
            await aexec(cmd, event)
        except Exception:
            exc = traceback.format_exc()
        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr
        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"
        final_output = f"•  Eval : \n`{cmd}` \n\n•  Result : \n`{evaluation}` \n"
        # await eor(
        # eviralevent,
        # "**Eval Command Executed. Check out LOGGER_ID Group[Private Group Where All Message Forward]for result.**",
        # )
        if "session" in cmd:
            await eor(
                event, "String is a  Sensetive Data.\nSo, Its Protected By FIREX"
            )
            return
        if "eviral_STRING" in cmd:
            await eor(
                event, "String is a  Sensetive Data.\nSo, Its Protected By FIREX"
            )
            return
        else:
            await eor(
                eviralevent,
                f"{final_output}",
            )
    else:
        await edit_or_reply(
            event,
            "If U Dont Know More About Then ask With Admin.\nTo Turn On ~  `.set var EVAL ON`",
        )


async def aexec(code, smessatatus):
    message = event = smessatatus
    p = lambda _x: print(yaml_format(_x))
    reply = await event.get_reply_message()
    exec(
        f"async def __aexec(message, event , reply, client, p, chat): "
        + "".join(f"\n {l}" for l in code.split("\n"))
    )
    return await locals()["__aexec"](
        message, event, reply, message.client, p, message.chat_id
    )


CMD_HELP.update(
    {
        "eval": "**Eval**\
\n\n**Syntax : **`.eval <python code>`\
\n**Usage :** Run python code using this plugin."
    }
)
