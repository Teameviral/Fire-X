import os
import re
from datetime import datetime

import requests

from firebot import CMD_HELP
from firebot.utils import admin_cmd

firethumb = "./resources/IMG_20210719_203714_817.jpg"


def main(url, filename):
    try:
        download_video("HD", url, filename)
    except (KeyboardInterrupt):
        download_video("SD", url, filename)


def download_video(quality, url, filename):
    html = requests.get(url).content.decode("utf-8")
    video_url = re.search(rf'{quality.lower()}_src:"(.+?)"', html).group(1)
    file_size_request = requests.get(video_url, stream=True)
    int(file_size_request.headers["Content-Length"])
    block_size = 1024
    with open(filename + ".mp4", "wb") as f:
        for data in file_size_request.iter_content(block_size):
            f.write(data)
    print("\nVideo downloaded successfully.")


@fire.on(admin_cmd(pattern="fbdl (.*)"))
async def _(event):
    if event.fwd_from:
        return
    url = event.pattern_match.group(1)
    x = re.match(r"^(https:|)[/][/]www.([^/]+[.])*facebook.com", url)

    if x:
        html = requests.get(url).content.decode("utf-8")
    else:
        await event.edit("This Video Is Either Private Or URL Is Invalid. Exiting... ")
        return

    _qualityhd = re.search('hd_src:"https', html)
    _qualitysd = re.search('sd_src:"https', html)
    _hd = re.search("hd_src:null", html)
    _sd = re.search("sd_src:null", html)

    list = []
    _thelist = [_qualityhd, _qualitysd, _hd, _sd]
    for id, val in enumerate(_thelist):
        if val != None:
            list.append(id)
    filename = datetime.strftime(datetime.now(), "%Y-%m-%d-%H-%M-%S")

    main(url, filename)
    await event.edit("Video Downloaded Successfully. Starting To Upload.")

    kk = f"{filename}.mp4"
    caption = (
        f"Facebook Video Successfully by Fire-X.\nGet Your Fire-X From @FIRE_X_CHANNEL."
    )

    await borg.send_message(
        event.chat_id,
        caption,
        thumb=firethumb,
        parse_mode="HTML",
        file=kk,
        force_document=True,
        allow_cache=False,
    )
    os.system(f"rm {kk}")


CMD_HELP.update(
    {
        "facebookDL": "**Facebook Video Downloader**\
\n\n**Syntax : **`.fbdl <video-link>`\
\n**Usage :** Downlosds The Facebook Video."
    }
)
