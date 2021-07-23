from telethon import events

from firebot import CMD_HELP


@fire.on(events.NewMessage(pattern=r"\.shout", outgoing=True))
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(" ".join([s for s in text]))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + " " + "  " * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`" + msg + "`")


CMD_HELP.update(
    {
        "shout": "**Shout**\
\n\n**Syntax : **`.shout <text>`\
\n**Usage :** Shouts a message in NEME way."
    }
)
