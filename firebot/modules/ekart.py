import requests

from firebot import CMD_HELP
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="ekart (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    urlo = (
        "https://track.aftership.com/trackings?courier=ekart&tracking-numbers="
        + str(input_str)
    )

    url = "https://ekart-api-chi.vercel.app/check?id=" + str(input_str)
    r = requests.get(url)
    h = r.json()
    merchant = h.get("merchant_name")
    order_status = h.get("order_status")
    kk = h.get("updates")
    oqwz = kk[0]
    aq = oqwz.get("Date")
    ar = oqwz.get("Time")
    place = oqwz.get("Place")
    status = oqwz.get("Status")

    caption = f""" <b>Ekart Tracking </b>
Merchant Name:- {merchant}
Order Status:- {order_status}
Tracking Id:- {input_str}
Latest Update
Date:- {aq}
Time:- {ar}
Place:- {place}
Status:- {status}
Detailed link:- {urlo}
<u><b>Ekart Search Completed By Fire-X.
"""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
    )
    await event.delete()


CMD_HELP.update(
    {
        "ekart_tracker": "**Ekat Tracker**\
\n\n**Syntax : **`.ekart <Tracking-ID>`\
\n**Usage :** Shows Details And Latest Updates About Given Tracking-ID."
    }
)
