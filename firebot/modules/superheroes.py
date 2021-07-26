import requests

from firebot.Configs import Config
from firebot.utils import admin_cmd


@fire.on(admin_cmd(pattern="hero (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    url = "https://superhero-search.p.rapidapi.com/"
    querystring = {"hero": input_str}
    if Config.SUPERHERO_API_KEY is None:
        await event.edit(
            "Need to get an API key from https://rapidapi.com/jakash1997/api/superhero-search\nModule stopping!"
        )
        return
    await event.edit("Processing Your Request.")
    inputo = Config.SUPERHERO_API_KEY

    headers = {
        "x-rapidapi-key": inputo,
        "x-rapidapi-host": "superhero-search.p.rapidapi.com",
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    a = response.json()
    b = a.get("name")
    c = a.get("id")
    d = a.get("slug")
    e = a.get("powerstats")
    intelligence = str(e.get("intelligence"))
    strength = str(e.get("strength"))
    speed = str(e.get("speed"))
    durability = str(e.get("durability"))
    power = str(e.get("power"))
    combact = str(e.get("combact"))
    f = a.get("appearance")
    lol = str(f.get("gender"))
    lul = str(f.get("race"))
    hm = f.get("height")
    inch = str(hm[0])
    cm = str(hm[1])
    # What are you doing in our code?

    weiGht = f.get("weight")
    lb = str(weiGht[0])
    kg = str(weiGht[1])
    eye = str(f.get("eyeColor"))
    hair = str(f.get("hairColor"))
    bio = a.get("biography")
    # Hey Kanger, Don't you dare Kamg this.

    fullName = str(bio.get("fullName"))
    ego = str(bio.get("alterEgos"))
    aliase = bio.get("aliases")
    sedo = ""
    # Messi Is The Best.
    for messi in aliase:
        sedo += messi + "   "

    PoB = str(bio.get("placeOfBirth"))
    sed = str(sedo)

    firsT = str(bio.get("firstAppearance"))

    alignment = str(bio.get("alignment"))

    imoge = a.get("images")
    res = list(imoge.keys())[3]
    linke = str(res)
    link = str(imoge.get(linke))
    fcb = input_str.upper()

    caption = f"""       <b>{fcb} STATS<b>
<b>Name:- </b>: <code>{b}</code>
<b>Id:- </b>: <code>{c}</code>
<b>Slug:- </b>: <code>{d}</code>
<u><b>Power Stats</b></u>
<b>Intelligence:- </b>: <code>{intelligence}</code>
<b>Strength:- </b>: <code>{strength}</code>
<b>Speed:- </b>: <code>{speed}</code>
<b>Durability:- </b>: <code>{durability}</code>
<b>Power:- </b>: <code>{power}</code>
<b>Combact:- </b>: <code>{combact}</code>
<u><b>Appearance</b></u>
<b>Gender:- </b>: <code>{lol}</code>
<b>Race:- </b>: <code>{lul}</code>
<b>Height:- </b>: <code>{inch}    {cm}</code>
<b>Weight:- </b>: <code>{lb}    {kg}</code>
<b>Eye Colour:- </b>: <code>{eye}</code>
<b>Hair Colour:- </b>: <code>{hair}</code>
<u><b>Biography</b></u>
<b>Full Name:- </b>: <code>{fullName}</code>
<b>Alter Egos:- </b>: <code>{ego}</code>
<b>Aliases:- </b>: <code>{sed}</code>
<b>Place Of Birth:- </b>: <code>{PoB}</code>
<b>First Appearance:- </b>: <code>{firsT}</code>
<b>alignment:- </b>: <code>{alignment}</code>
"""
    await borg.send_message(
        event.chat_id,
        caption,
        parse_mode="HTML",
        file=link,
        force_document=False,
        silent=True,
    )
    await event.delete()
