import cryptocompare

from firebot import CMD_HELP
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="crypto (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    stark = input_str.split(" ", 1)
    curreo = stark[0]
    currency1 = stark[1]
    curre = curreo.upper()
    currency = currency1.upper()
    take = ""
    take = cryptocompare.get_price(currency, curr=curre)
    t = take.get(currency)
    k = curre
    q = str(t.get(curre))

    await event.edit(
        f"<b><u>Conversion complete</b></u> \n<b>cryptocurrency</b>:-  <code>{currency}</code> \n<b>cryptocurrency value in </b> <code>{k}</code> <b> is :- </b> <code> {q}</code>",
        parse_mode="HTML",
    )


CMD_HELP.update(
    {
        "crypto": "**Cryptocurrency**\
\n\n**Syntax : **`.crypto <currency to give value in> <Cryptocurrency shortname>`\
\n**Usage :** Shows cryptocurrency value in given currency.\
\n\n**Example : **`.crypto inr btc`\
\nThis above syntax gives bitcoin's current value in INR."
    }
)
