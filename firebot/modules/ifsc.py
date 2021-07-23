import requests
from uniborg.util import fire_on_cmd

from firebot import CMD_HELP


@fire.on(fire_on_cmd(pattern="ifsc (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)

    IFSC_Code = input_str

    URL = "https://ifsc.razorpay.com/"

    data = requests.get(URL + IFSC_Code).json()

    a = data["ADDRESS"]
    b = data["CENTRE"]
    c = data["BRANCH"]
    d = data["CITY"]
    e = data["STATE"]
    f = data["BANK"]
    g = data["BANKCODE"]
    h = data["IFSC"]

    await event.edit(
        f"<b><u>INFORMATION GATHERED SUCCESSFULLY</b></u>\n\n<b>Bank Name :-</b><code>{f}</code>\n<b>Bank Address:- </b> <code>{a}</code>\n<b>Centre :-</b><code>{b}</code>\n<b>Branch :- </b><code>{c}</code>\n<b> City :-</b><code>{d}</code>\n<b>State:- </b> <code>{e}</code>\n<b>Bank Code :- </b><code>{g}</code>\n<b>Ifsc :-</b><code>{h}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "ifsc": "**IFSC**\
\n\n**Syntax : **`.ifsc <IFSC code>`\
\n**Usage :** gives you details about the bank."
    }
)
