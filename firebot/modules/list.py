import os

from uniborg.util import edit_or_reply, fire_on_cmd


@fire.on(fire_on_cmd(pattern="ls ?(.*)"))
@fire.on(fire_on_cmd(pattern="ls ?(.*)", allow_sudo=True))
async def lst(event):
    genesis = await edit_or_reply(event, "Processing")
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if input_str:
        msg = "**Files in {} :**\n".format(input_str)
        files = os.listdir(input_str)
    else:
        msg = "**Files in Current Directory :**\n"
        files = os.listdir(os.getcwd())
    for file in files:
        msg += "`{}`\n".format(file)
    if len(msg) <= Config.MAX_MESSAGE_SIZE_LIMIT:
        await genesis.edit(msg)
    else:
        msg = msg.replace("`", "")
        out = "filesList.txt"
        with open(out, "w") as f:
            f.write(f)
        await borg.send_file(
            event.chat_id,
            out,
            force_document=True,
            allow_cache=False,
            caption="`Output is huge. Sending as a file...`",
        )
        await event.delete()
