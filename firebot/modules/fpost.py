""" Command: .fpost word
credit: @pureindialover"""

import string

from uniborg.util import fire_on_cmd

msg_cache = {}


@fire.on(fire_on_cmd(pattern=r"fpost\s+(.*)"))
async def _(event):
    await event.delete()
    text = event.pattern_match.group(1)
    destination = await event.get_input_chat()

    for c in text.lower():
        if c not in string.ascii_lowercase:
            continue
        if c not in msg_cache:
            async for msg in borg.iter_messages(None, search=c):
                if msg.raw_text.lower() == c and msg.media is None:
                    msg_cache[c] = msg
                    break
        await borg.forward_messages(destination, msg_cache[c])
