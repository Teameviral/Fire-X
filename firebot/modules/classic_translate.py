""" Google Translate
Available Commands:
.translate LanguageCode as reply to a message
.translate LangaugeCode | text to translate"""

import emoji
from googletrans import Translator

from firebot.utils import admin_cmd, sudo_cmd 
from firebot import CMD_HELP

@bot.on(admin_cmd(pattern="translate ?(.*)"))
@bot.on(sudo_cmd(pattern="translate ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        # https://t.me/c/1220993104/192075
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await edit_or_reply(
            event,
            f"`.translate LanguageCode` as reply to a message.\nTry `.trn` to get all language codes",
        )
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
        # TODO: emojify the :
        # either here, or before translation
        output_str = """**Translated**\nFrom {} to {}
{}""".format(
            translated.src, lan, after_tr_text
        )
        await edit_or_reply(event, output_str)
    except Exception as exc:
        await edit_or_reply(event, str(exc))

@bot.on(admin_cmd(pattern=r"trn", outgoing=True))
@bot.on(sudo_cmd(pattern=r"trn", allow_sudo=True))
async def _(fire):
    if fire.fwd_from:
        return
    await edit_or_reply(fire, "**All The Language Codes Can Be Found** \n 🙂 [Here](https://telegra.ph/Chris-08-20) 🙂")



CMD_HELP.update(
    {
        "classic translate": ".tl <language code> <reply to text>"
        "\nUsage: reply any msg with .tr (language code) example .tr en / .tr hi\n\n"
        ".tl <language code> | <msg> "
        "\nUsage: translate text example .tr en|msg (note:- this | mark is important.\n\n"
    }
)
