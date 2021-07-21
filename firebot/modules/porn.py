# unban pornsites here
#
# lol jee lo apni zindagi
#
# HeHe created by @Black_lord_on_fire 
#
# 😂😂😂

import asyncio

from firebot import pro

from ..utils import admin_cmd

if pro == True:

    @borg.on(admin_cmd(pattern="porn"))
    async def _(event):  # @Black_lord_on_fire original

        if event.fwd_from:

            return

        animation_interval = 0.2

        animation_ttl = range(0, 8)

        await event.edit("`Connecting...`")

        animation_chars = [  # @Black_lord_on_fire original
            "P_",
            "PO_",
            "POR_",
            "PORN_",
            "PORNH_",
            "PORNHU_",
            "PORNHUB_",
            "[PORNHUB](www.porn93.cc)👄👅💦💦",  # @Black_lord_on_fire original
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 8])

    @borg.on(admin_cmd(pattern=r"xvideos"))
    async def _(event):

        if event.fwd_from:  # @Black_lord_on_fire original

            return

        animation_interval = 0.2

        animation_ttl = range(0, 7)

        await event.edit("`Connecting...`")

        animation_chars = [
            "X_",
            "XV_",
            "XVI_",
            "XVID_",
            "XVIDE_",
            "XVIDEO_",
            "[XVIDEOS](www.xvideos4.com)🖕👄💦💦",
        ]  # @Black_lord_on_fire original

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 7])

    import asyncio

    @borg.on(admin_cmd(pattern=r"xnxx"))  # @Black_lord_on_fire original
    async def _(event):

        if event.fwd_from:

            return

        animation_interval = 0.2

        animation_ttl = range(0, 5)

        await event.edit("`Connecting...`")  # @Black_lord_on_fire original

        animation_chars = [
            "X_",
            "XN_",
            "XNX_",
            "XNXX_",
            "[XNXX](www.xnxx.wapca.cc)👉🏻👌💦👄💦",
        ]
        # @Black_lord_on_fire original
        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 5])
