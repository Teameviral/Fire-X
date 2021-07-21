from datetime import datetime

from firebot.utils import edit_or_reply, fire_on_cmd


@fire.on(fire_on_cmd("gettime ?(.*)"))  # pylint:disable=E0602
async def gn(event):
    if event.fwd_from:
        return
    current_time = datetime.now().strftime(
        "CURRENT DATE & TIME \nLOCATION: Sri Lanka \nTime: %H:%M:%S \nDate: %d.%m.%y"
    )
    datetime.now()
    input_str = event.pattern_match.group(1)
    event.message.id
    if input_str:
        current_time = input_str
    elif event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        previous_message.id
    await edit_or_reply(
        event,
        current_time,
    )
