import asyncio
import io
import math
import os

import numpy as np
from pydub import AudioSegment
from telethon import types

from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="bassbost ?(.*)"))
async def __(message):
    v = False
    accentuate_db = 40
    reply = await message.get_reply_message()
    if not reply:
        await message.edit("Can You Reply To A MSG :?")
        return
    if message.pattern_match.group(1):
        ar = message.pattern_match.group(1)
        try:
            int(ar)
            if int(ar) >= 2 and int(ar) <= 100:
                accentuate_db = int(ar)
            else:
                await message.edit("`BassBost Level Should Be From 2 to 100 Only.`")
                return
        except Exception as exx:
            await message.edit("`SomeThing Went Wrong..` \n**Error:** " + str(exx))
            return
    else:
        accentuate_db = 2
    await message.edit("`Downloading This File...`")
    fname = await borg.download_media(message=reply.media)
    await message.edit("`BassBoosting In Progress..`")
    if fname.endswith(".oga") or fname.endswith(".ogg"):
        v = True
        audio = AudioSegment.from_file(fname)
    elif fname.endswith(".mp3") or fname.endswith(".m4a") or fname.endswith(".wav"):
        audio = AudioSegment.from_file(fname)
    else:
        await message.edit(
            "`This Format is Not Supported Yet` \n**Currently Supported :** `mp3, m4a and wav.`"
        )
        os.remove(fname)
        return
    sample_track = list(audio.get_array_of_samples())
    await asyncio.sleep(0.3)
    est_mean = np.mean(sample_track)
    await asyncio.sleep(0.3)
    est_std = 3 * np.std(sample_track) / (math.sqrt(2))
    await asyncio.sleep(0.3)
    bass_factor = int(round((est_std - est_mean) * 0.005))
    await asyncio.sleep(5)
    attenuate_db = 0
    filtered = audio.low_pass_filter(bass_factor)
    await asyncio.sleep(5)
    out = (audio - attenuate_db).overlay(filtered + accentuate_db)
    await asyncio.sleep(6)
    m = io.BytesIO()
    if v:
        m.name = "voice.ogg"
        out.split_to_mono()
        await message.edit("`Now Exporting...`")
        await asyncio.sleep(0.3)
        out.export(m, format="ogg", bitrate="64k", codec="libopus")
        await message.edit("`Process Completed. Uploading Now Here..`")
        await borg.send_file(
            message.to_id,
            m,
            reply_to=reply.id,
            voice_note=True,
            caption="Bass Boosted, \nDone By VirtualUserbot",
        )
        os.remove(m)
    else:
        m.name = "BassBoosted.mp3"
        await message.edit("`Now Exporting...`")
        await asyncio.sleep(0.3)
        out.export(m, format="mp3")
        await message.edit("`Process Completed. Uploading Now Here..`")
        await borg.send_file(
            message.to_id,
            m,
            reply_to=reply.id,
            attributes=[
                types.DocumentAttributeAudio(
                    duration=reply.document.attributes[0].duration,
                    title=f"BassBoost {str(accentuate_db)}lvl",
                    performer="BassBoost",
                )
            ],
            caption="Bass Boosted, \nDone By Fire-X",
        )
        os.remove(m)
    await message.delete()
    os.remove(fname)
