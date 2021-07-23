import os

from pdf2docx import parse

from firebot import CMD_HELP
from firebot.utils import fire_on_cmd

if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
    os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)


@fire.on(fire_on_cmd(pattern=r"pdf2docx"))
async def hmm(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Pdf File.")
        return
    await event.edit("hmm... Please Wait...🚶")
    lol = await event.get_reply_message()
    starky = await borg.download_media(lol.media, Config.TMP_DOWNLOAD_DIRECTORY)
    await event.edit("hmm... Please Wait..")
    pdf_file = starky
    docx_file = "./virtualuserbot/DOWNLOADS/Infinity_Bots.docx"
    parse(pdf_file, docx_file, start=0, end=None)
    await borg.send_file(
        event.chat_id,
        docx_file,
        caption=f"*PDF Converted Into Docx by VirtualUserbot. Credits to @FRIDAYOT.",
    )
    os.remove(pdf_file)
    os.remove(docx_file)
    await event.delete()


CMD_HELP.update(
    {
        "fileTools": "**File Tools**\
\n\n**Syntax : **`.pdf2docx <reply to pdf>`\
\n**Usage :** Converts Given Pdf Into Docx.\
\n\n**Syntax : **`.p2dcl <channel username>`\
\n**Usage :** Converts All The Pdf's From Channel Into Docx."
    }
)
