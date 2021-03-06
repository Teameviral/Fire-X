import asyncio

from telethon.events import ChatAction, NewMessage
from telethon.tl.types import MessageEntityMentionName

from firebot import CMD_HELP
from firebot.function import get_all_admin_chats, is_admin
from firebot.modules.sql_helper import gban_sql
from firebot.modules.sql_helper.mute_sql import is_muted, mute, unmute
from firebot.utils import fire_on_cmd


@fire.on(fire_on_cmd(pattern="gban(?: |$)(.*)"))
async def gbun(event):
    await event.edit("**GBanning User**")
    sucess = 0
    bad = 0
    user, reason = await get_user_from_event(event)
    if not user.id:
        await event.edit("`Mention A User To Gban`")
        return
    if not reason:
        hmm_r = "#GBanned"
    elif reason:
        hmm_r = reason
    if user.id == bot.uid:
        await event.edit("**I Can't Gban You Master :(**")
        return
    if gban_sql.is_gbanned(user.id):
        await event.edit(
            "**This User Is Already Gbanned. No Point In Gbanning Him Again !**"
        )
        return
    gban_sql.gban_user(user.id, hmm_r)
    chat_s = await get_all_admin_chats(event)
    if len(chat_s) == 0:
        await event.edit(
            "**You Need To Be Admin In Atleast 1 Group To Perform this Action**"
        )
        return
    len_s = len(chat_s)
    await event.edit(
        f"**GBanning !** [{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**"
    )
    for stark_s in chat_s:
        try:
            await event.client.edit_permissions(stark_s, user.id, view_messages=False)
            sucess += 1
        except:
            bad += 0
    await event.edit(
        f"**GBanned !**[{user.first_name}](tg://user?id={user.id}) **in {sucess} Chats!**"
    )


@fire.on(fire_on_cmd(pattern="ungban(?: |$)(.*)"))
async def ungbun(event):
    await event.edit("**Un-GBanning User**")
    sucess = 0
    bad = 0
    user, reason = await get_user_from_event(event)
    if not user.id:
        await event.edit("`Mention A User To Un-Gban`")
        return
    if user.id == bot.uid:
        await event.edit("**I Can't Un-Gban You Master :(**")
        return
    if not gban_sql.is_gbanned(user.id):
        await event.edit("**This User Is Not Gbanned. No Point In Un-Gbanning !**")
        return
    gban_sql.ungban_user(user.id)
    chat_s = await get_all_admin_chats(event)
    if len(chat_s) == 0:
        await event.edit(
            "**You Need To Be Admin In Atleast 1 Group To Perform this Action**"
        )
        return
    len_s = len(chat_s)
    await event.edit(
        f"**Un-GBanning !** [{user.first_name}](tg://user?id={user.id}) **in {len_s} Chats!**"
    )
    for stark_s in chat_s:
        try:
            await event.client.edit_permissions(stark_s, user.id, view_messages=True)
            sucess += 1
        except:
            bad += 0
    await event.edit(
        f"**Un-GBanned !**[{user.first_name}](tg://user?id={user.id}) **in {sucess} Chats!**"
    )


@fire.on(ChatAction)
async def starky(event):
    if event.user_joined:
        hmm = await bot.get_me()
        if await is_admin(event, hmm.id):
            sadly = await event.get_user()
            if gban_sql.is_gbanned(sadly.id):
                try:
                    await event.client.edit_permissions(
                        event.chat_id, sadly.id, view_messages=False
                    )
                    await event.reply(
                        f"**#GBanned-User** \nUserID : {sadly.id} \nReason : {gban_sql.is_gbanned(sadly.id)}"
                    )
                except:
                    pass


@fire.on(NewMessage)
async def mi(event):
    sed = event.sender_id
    hmm = await bot.get_me()
    if event.is_private:
        return
    if await is_admin(event, hmm.id):
        if gban_sql.is_gbanned(sed):
            try:
                await event.client.edit_permissions(
                    event.chat_id, sed, view_messages=False
                )
            except:
                pass


async def get_user_from_event(event):
    """Get the user from argument or replied message."""
    args = event.pattern_match.group(1).split(" ", 1)
    extra = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.sender_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]

        if user.isnumeric():
            user = int(user)

        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj

        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    elif event.is_private:
        hmm = await event.get_input_chat()
        try:
            user_obj = await event.client.get_entity(hmm)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
        extra = event.pattern_match.group(1)
    return user_obj, extra


async def get_user_sender_id(user, event):
    if isinstance(user, str):
        user = int(user)

    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None

    return user_obj


@fire.on(fire_on_cmd(pattern=r"gmute ?(\d+)?"))
async def startgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to gmute them."
        )
    event.chat_id
    await event.get_chat()
    if is_muted(userid, "gmute"):
        return await event.edit("`He has Tap Already On His Mouth.`")
    try:
        mute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Here A Tape, Now Shutup \nGmuteD")


@fire.on(fire_on_cmd(pattern=r"ungmute ?(\d+)?"))
async def endgmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.edit("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    reply = await event.get_reply_message()
    if event.pattern_match.group(1) is not None:
        userid = event.pattern_match.group(1)
    elif reply is not None:
        userid = reply.sender_id
    elif private is True:
        userid = event.chat_id
    else:
        return await event.edit(
            "Please reply to a user or add their into the command to ungmute them."
        )
    event.chat_id
    if not is_muted(userid, "gmute"):
        return await event.edit("This user is not gmuted")
    try:
        unmute(userid, "gmute")
    except Exception as e:
        await event.edit("Error occured!\nError is " + str(e))
    else:
        await event.edit("Successfully ungmuted that person")


@command(incoming=True)
async def watcher(event):
    if is_muted(event.sender_id, "gmute"):
        await event.delete()


CMD_HELP.update(
    {
        "gtools": "**Global Tools**\
\n\n**Syntax : **`.gmute <replying to user message>`\
\n**Usage :** Gmute User And Delete His Msg.\
\n\n**Syntax : **`.ungmute <replying to user message>`\
\n**Usage :** UnGmute User And Stops Deleting His Msgs.\
\n\n**Syntax : **`.gban <replying to user message>`\
\n**Usage :**  Gban User And Blow Him From Your Groups\
\n\n**Syntax : **`.ungban <replying to user message>`\
\n**Usage :** Ugban User."
    }
)
