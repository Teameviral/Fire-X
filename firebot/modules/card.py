from faker import Faker as dc

from firebot import bot as firebot

from ..utils import admin_cmd as wtf


@firebot.on(wtf("card"))
async def _firee(fire):
    cyber = dc()
    killer = cyber.name()
    kali = cyber.address()
    chris = cyber.credit_card_full()
    await fire.edit(f"ℕ𝕒𝕞𝕖:-\n`{killer}`\n\n𝔸𝕕𝕕𝕣𝕖𝕤𝕤:-\n`{kali}`\n\nℂ𝕒𝕣𝕕:-\n`{chris}`")
