"""

Available Commands:

.sux

.fuuk

.kiss"""


import asyncio
import random
from asyncio import sleep

from firebot import CMD_HELP, bot

from ..utils import admin_cmd, edit_or_reply, sudo_cmd

img1 = "https://t.me/danish2512/2"
img2 = "https://t.me/danish2512/3"
img3 = "https://t.me/danish2512/4"
img4 = "https://t.me/danish2512/5"
img5 = "https://t.me/danish2512/6"
img6 = "https://t.me/danish2512/7"
img7 = "https://t.me/danish2512/8"
img8 = "https://t.me/danish2512/9"
img9 = "https://t.me/danish2512/10"
img10 = "https://t.me/danish2512/11"
img11 = "https://t.me/danish2512/12"
img12 = "https://t.me/danish2512/13"
img13 = "https://t.me/danish2512/14"
img14 = "https://t.me/danish2512/15"
img15 = "https://t.me/danish2512/16"
img16 = "https://t.me/danish2512/17"
img17 = "https://t.me/danish2512/18"
img18 = "https://t.me/danish2512/19"
img19 = "https://t.me/danish2512/20"
img20 = "https://t.me/danish2512/21"
img21 = "https://t.me/danish2512/22"
img22 = "https://t.me/danish2512/23"
img23 = "https://t.me/danish2512/24"
img24 = "https://t.me/danish2512/25"
img25 = "https://t.me/danish2512/26"
img26 = "https://t.me/danish2512/27"
img27 = "https://t.me/danish2512/28"
img28 = "https://t.me/danish2512/29"
img29 = "https://t.me/danish2512/30"
img30 = "https://t.me/danish2512/31"


RUNSTRINGS = (
    "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
    "❤ ආදලෙයි 150GB ක්!! ❤",
    "ඕයි...! පෙට්ටිය කැඩුවනම් දැන් ලමය බාරගනින්!!",
    "තමුසෙ පිස්සෙක්නෙ ඕයි!",
    "මොනාද හුත්තෝ බලන්නේ...??",
    "කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!!",
    "හායි!! කෝමද පැටියෝ ❣❣",
    "මැරිලත් පැය හතරක් ආදරෙයි.. අම්මපා",
    "ටෞකන්ඩ මූ යකෝ!!",
    "ඔයා අදත් මට අර යෝගට් පානය දෙනවද...?",
    "චූ කරල නිදාගනින් අයියේ...",
    "ඔයා හරි සෝයි අනේ.. සෝ කියුට්... 😋",
    "අපි දෙන්න පැනල යමු.. හාද?? . ",
    "පල යන්න වේසාවෝ!!",
    "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
    "අඩ්ඩේහ්..! මේ මොකද කරන්නේ??",
    "පොඩිකාලෙ බිව්වෙ පොල්කිරිද මල්ලී 🤑",
    "සීනි කන්න ආපු කූඹියො නෙමෙයි සීනි බෝතලේ ඇරපු ඔයයි වැරදි..",
    "කවුරු කොහොම් කිව්වත් \nකොත්තු කෑවොත් බඩ යන එක යනවමයි!",
    "ආදරෙයි.. මැණික ❤❤",
    "❤ ආදලෙයි 250GB ක්!! ❤",
    "හදුන්වාදෙන වැඩි දිගකින් යුත් fens.. \nභාවිත කර බලා වෙනස හඳුනාගන්න!",
    "ඔයාට suprise එකක් තියෙයි.. /kickme කියල ගහල බලන්නකෝ 😂",
    "ට්‍රැක්ටරය පැදවීමට මාගේ ඡායාරූප භාවිත කිරීමෙන් වලකින්න ",
    "ඔයාට suprise එකක් තියෙයි.. /kickme කියල ගහල බලන්නකෝ 😂",
    "මූ හුත්තෝ..",
    "මොන හුයන්නක්ද මේ",
    "පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල",
    "ටොයිලට් එකේ ඉද්දි හෙඩ්සෙට් එක ගහන් සින්දු අහන්න එපා ඕයි...",
    "බලු කූඩුව ඇරියෙ මොකාද යකෝ!!",
    "බය තරහ ඇති කරවයි. තරහ වයිරය උපදවයි. වරිරය පසුතැවීම ඇති කරයි. ඔබ බයෙන් ජීවත්වන තුරු ලංකාවේ බඩු මිල පහත නොයයි",
    "රට්ටු හිනස්සන්න එපා මල්ලී.",
    "හදිසි අවස්තාවකදී ගිලන්රථයක් ගෙන්වා ගැනීමට 1990 අමතන්න",
    "අපේ ගෲප් එකත් එක්ක අදම සෙට් වෙන්න t.me/InfinityJE ❤",
    "ඔයාට කොච්චර සල්ලි තිබුනත් කොච්චර බලය තිබුනත් කොත්තු කෑවොත් බඩ යන එක නවත්තන්න ඔයාට බෑ 🌮🌮.",
    "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
    "ටෞකන්ඩ මූ යකෝ!!!",
    "කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!",
    "පොඩිකාලෙ බිව්වෙ පොල්කිරිද මල්ලී 🤑",
    "කවුරු කොහොම් කිව්වත් \nකොත්තු කෑවොත් බඩ යන එක යනවමයි!",
    "රට්ටු හිනස්සන්න එපා මල්ලී.",
    "ආදරෙයි.. මැණික ❤❤",
    "💔 මල්ලියෝ!! ම්ං අර දෙන්නෙක්ට ආදරේ කරේ නෑනේ සුදු මල්ලියෝ!! 💔",
)


@bot.on(admin_cmd(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.1

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "fuuk":

        await event.edit(input_str)

        animation_chars = ["👉       ✊️", "👉     ✊️", "👉  ✊️", "👉✊️💦"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "sux":

        await event.edit(input_str)

        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵👼👰"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


""


@bot.on(admin_cmd(pattern=r"(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.2

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "kiss":

        await event.edit(input_str)

        animation_chars = ["🤵       👰", "🤵     👰", "🤵  👰", "🤵💋👰"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 4])


@bot.on(admin_cmd(pattern="kp$"))
@bot.on(sudo_cmd(pattern="kp$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** කැරි පකයා **",
    )


from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="slo$"))
@bot.on(sudo_cmd(pattern="slo$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල😎 **",
    )


@bot.on(admin_cmd(pattern="hp$"))
@bot.on(sudo_cmd(pattern="hp$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** හුත්තිගෙ පුතා **",
    )


@bot.on(admin_cmd(pattern="hu$"))
@bot.on(sudo_cmd(pattern="hu$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!😂😂**",
    )


@bot.on(admin_cmd(pattern="sm$"))
@bot.on(sudo_cmd(pattern="sm$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** එහෙම එවා නෑ පුතා..😍 ඒ සෙලවෙන මනස **",
    )


@bot.on(admin_cmd(pattern="fk$"))
@bot.on(sudo_cmd(pattern="fk$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "**පල හුත්තෝ යන්න 😂\n තෝ සමාජයට විහිළුවක් ඕයි 😒**",
    )


@bot.on(admin_cmd(pattern="tah$"))
@bot.on(sudo_cmd(pattern="tah$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** ටහුකන්න අලංකාර 😐🤚**",
    )


@bot.on(admin_cmd(pattern="bs$"))
@bot.on(sudo_cmd(pattern="bs$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** Good Night 🌙 Bs ☸️ Jp ✝️Tc 😘Byee...👋👋👋👋 **",
    )


@bot.on(admin_cmd(pattern="aks$"))
@bot.on(sudo_cmd(pattern="aks$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** අනියම් කාම සේවනය තරයේ හෙලා දකිමි 🙈 **",
    )


@bot.on(admin_cmd(pattern="ja$"))
@bot.on(sudo_cmd(pattern="ja$", allow_sudo=True))
async def gn(event):
    await edit_or_reply(
        event,
        "** ජීවිතය අනියතය..☹️ මරණය නියතය 🙏 මහනවීම සැපය 🙏**",
    )


@bot.on(admin_cmd(pattern=f"srun$", outgoing=True))
@bot.on(sudo_cmd(pattern="snun$", allow_sudo=True))
async def runstrings(event):
    txt = random.choice(RUNSTRINGS)
    await edit_or_reply(event, txt)


from firebot import CMD_HELP


@bot.on(admin_cmd("newyear"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 80)
    await event.edit("😊 HAPPY NEW YEAR 😁")
    animation_chars = [
        "💖HAPPY NEW YEAR💖",
        "💙HAPPY NEW YEAR💙",
        "❤️HAPPY NEW YEAR❤️",
        "💚HAPPY NEW YEAR💚",
        "💜HAPPY NEW YEAR💜",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 5])


@bot.on(admin_cmd("happynewyear"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(0, 22)
    await event.edit("😊 HAPPY NEW YEAR TO ALL 😁")
    animation_chars = [
        """💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜💜💜💜💜💜💜💜
💜💜💜💜💜💜💜💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜
💜💜                        💜💜""",
        """ㅤㅤㅤㅤㅤ ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤ
                    💙💙
                 💙💙💙
             💙💙💙💙
            💙💙 💙💙
          💙💙    💙💙
        💙💙       💙💙
     💙💙💙💙💙💙
      💙💙💙💙💙💙
   💙💙                 💙💙
  💙💙                    💙💙
💙💙                       💙💙""",
        """💚💚💚💚💚💚💚
💚💚💚💚💚💚💚💚
💚💚                     💚💚
💚💚                     💚💚
💚💚💚💚💚💚💚💚
💚💚💚💚💚💚💚
💚💚
💚💚
💚💚
💚💚""",
        """💛💛💛💛💛💛
💛💛💛💛💛💛💛
💛💛                💛💛
💛💛                💛💛
💛💛💛💛💛💛💛
💛💛💛💛💛💛
💛💛
💛💛
💛💛
💛💛""",
        """💜💜                    💜💜
   💜💜              💜💜
      💜💜        💜💜
         💜💜  💜💜
            💜💜💜
              💜💜
              💜💜
              💜💜
              💜💜
              💜💜""",
        """😺😺                           😺😺
😺😺😺                       😺😺
😺😺😺😺                 😺😺
😺😺  😺😺               😺😺
😺😺     😺😺            😺😺
😺😺         😺😺        😺😺
😺😺             😺😺    😺😺
😺😺                 😺😺😺😺
😺😺                     😺😺😺
😺😺                          😺😺
⁭""",
        """😁😁😁😁😁😁😁😁
😁😁😁😁😁😁😁😁
😁😁
😁😁
😁😁😁😁😁😁
😁😁😁😁😁😁
😁😁
😁😁
😁😁😁😁😁😁😁😁
😁😁😁😁😁😁😁😁""",
        """🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳                               🥳🥳
🥳🥳              🥳            🥳🥳
 🥳🥳           🥳🥳          🥳🥳
 🥳🥳        🥳🥳🥳       🥳🥳
  🥳🥳   🥳🥳  🥳🥳   🥳🥳
   🥳🥳🥳🥳      🥳🥳🥳🥳
    🥳🥳🥳             🥳🥳🥳""",
        """🌈🌈                    🌈🌈
   🌈🌈              🌈🌈
      🌈🌈        🌈🌈
         🌈🌈  🌈🌈
            🌈🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈
              🌈🌈""",
        """🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊
🎊🎊
🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊
🎊🎊
🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊
🎊🎊🎊🎊🎊🎊🎊🎊""",
        """⁭
                    ㅤ
                  🎉🎉
               🎉🎉🎉
            🎉🎉 🎉🎉
          🎉🎉    🎉🎉
        🎉🎉       🎉🎉
      🎉🎉🎉🎉🎉🎉
     🎉🎉🎉🎉🎉🎉🎉
   🎉🎉                 🎉🎉
  🎉🎉                    🎉🎉
🎉🎉                       🎉🎉""",
        """⁭
🕉🕉🕉🕉🕉🕉🕉
🕉🕉🕉🕉🕉🕉🕉🕉
🕉🕉                     🕉🕉
🕉🕉                     🕉🕉
🕉🕉🕉🕉🕉🕉🕉🕉
🕉🕉🕉🕉🕉🕉🕉
🕉🕉    🕉🕉
🕉🕉         🕉🕉
🕉🕉              🕉🕉
🕉🕉                  🕉🕉""",
    ]
    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 12])


@bot.on(admin_cmd(pattern=f"cyfile$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"cyfile$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "cyfiles")
    await event.edit("❄️ **Disconnected**")
    await asyncio.sleep(2)
    await event.edit("🌩 **Connecting.**")
    await asyncio.sleep(0.5)
    await event.edit("🌧 **Connecting..**")
    await asyncio.sleep(0.5)
    await event.edit("🌩 **Connecting...**")
    await asyncio.sleep(0.5)
    await event.edit("🌧 **Connecting.**")
    await asyncio.sleep(0.5)
    await event.edit("🌩 **Connecting..**")
    await asyncio.sleep(0.5)
    await event.edit("🌧 **Connecting...**")
    await asyncio.sleep(0.5)
    await event.edit("💥 **Connection Established**")
    await asyncio.sleep(1)
    await event.edit("☁️ ** VPN Connected**")
    await asyncio.sleep(2)


@bot.on(admin_cmd(pattern=f"fileunlock$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"fileunlock$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "fileunlock")
    await event.edit("📁 **File name : Dialog 0 Balance**")
    await asyncio.sleep(1)
    await event.edit("🔓 **Begin unlocking file...**")
    await asyncio.sleep(1)
    await event.edit("🔓 **Unlocked 50%**")
    await asyncio.sleep(0.5)
    await event.edit("🔓 **Unlocked 100%**")
    await asyncio.sleep(0.5)
    await event.edit("**Please do no share this host for longer use !!**")
    await asyncio.sleep(1)
    await event.edit(
        "**Your Host securaly stored. Get it from below link 👇\nhttps://telegra.ph/Dialog-Host-01-12**"
    )
    await asyncio.sleep(2)


@bot.on(admin_cmd(pattern=f"freenet$", outgoing=True))
@bot.on(sudo_cmd(pattern=f"freenet$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    event = await edit_or_reply(event, "freenet")
    await event.edit("**Connecting to Singapore Server 🇸🇬**")
    await asyncio.sleep(1)
    await event.edit("**Successfully Connected 💯**")
    await asyncio.sleep(1)
    await event.edit("**හරි පුතේ එල අය ඔයාගේ data කැපෙන්නේ නෑ 👌**")
    await asyncio.sleep(1)


@bot.on(admin_cmd(pattern=r"ehu$"))
@bot.on(sudo_cmd(pattern=r"ehu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(18)
    event = await edit_or_reply(event, "Connecting to Http Injector......")
    animation_chars = [
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested`""",
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X UB"
[2021-01-12 16:58:55] Injector Service Started`""",
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "VirtualUserbot"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection`""",
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting`""",
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "VirtualUserbot"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256`""",
        """`[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-shad256`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: Fire-X
[16:58:58] Server Message:
⚡️ Fire-X Server 🎮&nbsp;
🔥 Powered By FIRE-X USERBOT 
☬ Special Thanks To My Master
`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: Fire-X
[16:58:58] Server Message:
⚡️ Fire-X Server 🎮&nbsp;
🔥 Powered By FIRE-X UB 
☬ Special Thanks To My Master
⭕️ NO DDOS !!!
⭕️ NO FRAUD !!!
⭕️ NO CARDING !!!
⭕️ NO HACKING !!!
⭕️ NO TORRENT !!!
⭕️ NO SPAMMING !!!
⭕️ THIS IS NOT FOR SALE !!!⭕️ NO ILLEGAL ACTIVITES !!!
⭕️ AUTO REBOOT @ MIDNIGHT !!!
⭕️Do Not Over Use This Service⭕️⚒ Configured by Fire-X
`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "Fire-X"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: Fire-X
[16:58:58] Server Message:
⚡️ Fire-x Server 🎮&nbsp;
🔥 Powered By FIREBOT 
☬ Special Thanks To My Master
⭕️ NO DDOS !!!
⭕️ NO FRAUD !!!
⭕️ NO CARDING !!!
⭕️ NO HACKING !!!
⭕️ NO TORRENT !!!
⭕️ NO SPAMMING !!!
⭕️ THIS IS NOT FOR SALE !!!⭕️ NO ILLEGAL ACTIVITES !!!
⭕️ AUTO REBOOT @ MIDNIGHT !!!
⭕️Do Not Over Use This Service⭕️⚒ Configured by FIREXUB



 Password auth available
[ 16:58:58] Authenticate with password
[ 16:58:59] Forward Successful
[ 16:58:59] Connected
`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "FIRE-X UB"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: FIRE-X UB
[16:58:58] Server Message:
⚡️ FIRE-X UB Server 🎮&nbsp;
🔥 Powered By FIRE-X UB 
☬ Special Thanks To My Master
⭕️ NO DDOS !!!
⭕️ NO FRAUD !!!
⭕️ NO CARDING !!!
⭕️ NO HACKING !!!
⭕️ NO TORRENT !!!
⭕️ NO SPAMMING !!!
⭕️ THIS IS NOT FOR SALE !!!⭕️ NO ILLEGAL ACTIVITES !!!
⭕️ AUTO REBOOT @ MIDNIGHT !!!
⭕️Do Not Over Use This Service⭕️⚒ Configured by VirtualUserbot  



 Password auth available
[ 16:58:58] Authenticate with password
[ 16:58:59] Forward Successful
[ 16:58:00] Connected
`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "FIRE-X UB"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: FIRE-X UB
[16:58:58] Server Message:
⚡️ FIRE-X UB Server 🎮&nbsp;
🔥 Powered By FIRE-X UB 
☬ Special Thanks To My Master
⭕️ NO DDOS !!!
⭕️ NO FRAUD !!!
⭕️ NO CARDING !!!
⭕️ NO HACKING !!!
⭕️ NO TORRENT !!!
⭕️ NO SPAMMING !!!
⭕️ THIS IS NOT FOR SALE !!!⭕️ NO ILLEGAL ACTIVITES !!!
⭕️ AUTO REBOOT @ MIDNIGHT !!!
⭕️Do Not Over Use This Service⭕️⚒ Configured by VirtualUserbot  



 Password auth available
[ 16:58:58] Authenticate with password
[ 16:58:59] Forward Successful
[ 16:58:59] Connected
[ 16:58:59] Starting Injector VPN Service
[ 16:58:59] Network available: [type: WIFI[] - WIFI, state: CONNECTED/CONNECTED, reason: (unspecified), extra: "FIRE-X UB", roaming: false, failover: false, isAvailable: true]
[ 16:58:59] DNS Forwarding: Google DNS
[ 16:58:59] Preparing DNS forwarding
[ 16:59:00] Starting DNS forwarding
[ 16:59:00] Google DNS enabled
[ 16:59:00] DNS forwarding enabled
[ 16:59:00] Routes: 0.0.0.0/0, 8d.8.4.4/32, 8.8.8.8/32 
`""",
        """`
[ 16:58:55] Tunnel Type HTTP Proxy ➔ SSH (Custom Payload)
[ 16:58:55] [START] service requested
[ 16:58:55] Network Status: CONNECTED  to WIFI "FIRE-X UB"
[2021-01-12 16:58:55] Injector Service Started
[ 16:58:55] Local IP: 192.188.800.100
[ 16:58:55] Starting listening local port: 8989
[ 16:58:55] Starting - Network Task
[ 16:58:55] Remote Proxy Address:140.238.246.145:8080
[ 16:58:55] Listening for incoming connection
[ 16:58:56] Start tunnel service
[ 16:58:57] Buffer Size: Send: 16384 | Receive: 32768
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] Running - Proxy Thread
[ 16:58:57] locked Payload
[ 16:58:57] Injecting
] Status: 200 (Connection established) Successful - The action requested by the client was successful.
[16:58:58] Hostkey fingerprint: 94:20:97:11:83:fd:f7:ca:c6:0d:61:17:79:5d:51:e3
[16:58:58] Key exchange algorithm: curve25519-sha256
[16:58:58] Using algorithm: aes256-ctr hmac-sha2-256-etm@sh.com
[2021-01-12 16:58:58] Username: FIRE-X UB
[16:58:58] Server Message:
⚡️ FIRE-X UB Server 🎮&nbsp;
🔥 Powered By FIRE-X UB 
☬ Special Thanks To My Master
⭕️ NO DDOS !!!
⭕️ NO FRAUD !!!
⭕️ NO CARDING !!!
⭕️ NO HACKING !!!
⭕️ NO TORRENT !!!
⭕️ NO SPAMMING !!!
⭕️ THIS IS NOT FOR SALE !!!⭕️ NO ILLEGAL ACTIVITES !!!
⭕️ AUTO REBOOT @ MIDNIGHT !!!
⭕️Do Not Over Use This Service⭕️⚒ Configured by VirtualUserbot  



 Password auth available
[ 16:58:58] Authenticate with password
[ 16:58:59] Forward Successful
[ 16:58:59] Connected
[ 16:58:59] Starting Injector VPN Service
[ 16:58:59] Network available: [type: WIFI[] - WIFI, state: CONNECTED/CONNECTED, reason: (unspecified), extra: "FIRE-X UB", roaming: false, failover: false, isAvailable: true]
[ 16:58:59] DNS Forwarding: Google DNS
[ 16:58:59] Preparing DNS forwarding
[ 16:59:00] Starting DNS forwarding
[ 16:59:00] Google DNS enabled
[ 16:59:00] DNS forwarding enabled
[ 16:59:00] Routes: 0.0.0.0/0, 8.8.4.4/32, 8.8.8.8/32 
[ 16:59:00] Routes excluded: 10.0.0.0/8, 140.238.246.145/32, 172.16.0.0/12, 192.168.0.0/16 
[ 16:59:01] VPN Connected
[ 16:59:02] Type: WIFI | State: CONNECTED | "FIRE-X UB"
`""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 18])


@borg.on(admin_cmd(outgoing=True, pattern="merrychristmas"))
async def _(event):

    if event.fwd_from:
        return
    await event.edit("**.\n\n😊 ℍ𝕠 ℍ𝕠 ℍ𝕠... 🎅🏻\n\n.**")
    await sleep(1.6)
    await event.edit("🎉")
    await sleep(3)
    await event.edit("🎊")
    await sleep(3)
    await event.edit("💔")
    await sleep(1.5)
    await event.edit("❤")
    await sleep(3)
    await event.edit(".\n\n\n😊𝓜𝓔𝓡𝓡𝓨 𝓒𝓗𝓡𝓘𝓢𝓣𝓜𝓐𝓢😁\n\n\n.")
    await sleep(3)
    await event.edit("🥳")
    await sleep(3.3)
    await event.edit("⛄")
    await sleep(3.4)
    await event.edit("🌨🌨🌨🌨🌨\n\n❄❄❄❄❄\n❄️❄️❄️❄️❄️")
    await sleep(2.8)
    await event.edit("☃️")
    await sleep(3.7)
    await event.edit("🥶")
    await sleep(3.7)
    await event.edit("🎄")
    await sleep(3.2)
    await event.edit(".\n\n\n**𝐌𝒆𝒓𝒓𝒚 𝑪𝒉𝒊𝒔𝒕𝒎𝒂𝒔😊😊**\n\n\n.")
    await sleep(2.9)
    danish = await bot.send_file(event.chat_id, "https://t.me/mcmc2021/36")
    await sleep(4)
    x = random.randrange(0, 30)
    if x == 1:
        await bot.send_file(event.chat_id, img1)

    if x == 2:
        await bot.send_file(event.chat_id, img2)

    if x == 3:
        await bot.send_file(event.chat_id, img3)

    if x == 4:
        await bot.send_file(event.chat_id, img4)

    if x == 5:
        await bot.send_file(event.chat_id, img5)

    if x == 6:
        await bot.send_file(event.chat_id, img6)

    if x == 7:
        await bot.send_file(event.chat_id, img7)

    if x == 8:
        await bot.send_file(event.chat_id, img8)

    if x == 9:
        await bot.send_file(event.chat_id, img9)

    if x == 10:
        await bot.send_file(event.chat_id, img10)

    if x == 11:
        await bot.send_file(event.chat_id, img11)

    if x == 12:
        await bot.send_file(event.chat_id, img12)

    if x == 13:
        await bot.send_file(event.chat_id, img13)

    if x == 14:
        await bot.send_file(event.chat_id, img14)

    if x == 15:
        await bot.send_file(event.chat_id, img15)

    if x == 16.0:
        await bot.send_file(event.chat_id, img16)

    if x == 17:
        await bot.send_file(event.chat_id, img17)

    if x == 18:
        await bot.send_file(event.chat_id, img18)

    if x == 19:
        await bot.send_file(event.chat_id, img19)

    if x == 20:
        await bot.send_file(event.chat_id, img20)

    if x == 21:
        await bot.send_file(event.chat_id, img21)

    if x == 22:
        await bot.send_file(event.chat_id, img22)

    if x == 23:
        await bot.send_file(event.chat_id, img23)

    if x == 24:
        await bot.send_file(event.chat_id, img24)

    if x == 25:
        await bot.send_file(event.chat_id, img25)

    if x == 26:
        await bot.send_file(event.chat_id, img26)

    if x == 27:
        await bot.send_file(event.chat_id, img27)

    if x == 28:
        await bot.send_file(event.chat_id, img28)

    if x == 29:
        await bot.send_file(event.chat_id, img29)

    if x == 30:
        await bot.send_file(event.chat_id, img30)


CMD_HELP.update(
    {
        "Sinhala_Jokes": "\n**Config Fun**\n\n.freenet `- fun`\n.ehu `- Ehi file connecting`\n.cyfiles `- cyh connecting`\n\n**RUN STRINGS**\n.srun -  Run Strings to FIRE-X UB 😂..\n\n**Nothing to Say**\n.boobs\n.butts\n\n**Funny Animations.**\n.fuuk\n.sux\n.kiss\n.lovestory\n.gdbye\n.hbty\n.merrychristmas\n.bs\n\n**Frequently using quotes\n.hu - `කවුරුන් කෙසේ කීවද ඵරුස වචන භාවිතය ඔබේ අරක පණ නැති කරවයි!`\n.slo -  `පෝන් එක හිරවෙනවාද?? ගලක්මත තබා හොඳින් තලන්න නිසැක ප්‍රතිඵල`\n.hp - `හුත්තිගෙ පුතා`\n.kp - `කැරි පකයා`\n.sm - `එහෙම එවා නෑ පුතා.ඒ සෙලවෙන මනස`\n.fk - `පල හුත්තෝ යන්න. තෝ සමාජයට විහිලුවක් ඕයි`\n.aks - `අනියම් කාම සේවනය තරයේ හෙලා දකිමි`\n.ja - `ජීවිතය අනියතය.. මරණය නියතය  මහනවීම සැපය `\n.tah - `ටහුකන්න අලංකාර`"
    }
)
