from covid import Covid

from firebot import CMD_HELP

from ..utils import admin_cmd, edit_or_reply, sudo_cmd


@bot.on(admin_cmd(pattern="covid(?: |$)(.*)"))
@bot.on(sudo_cmd(pattern="covid(?: |$)(.*)", allow_sudo=True))
async def corona(event):
    if event.pattern_match.group(1):
        country = (event.pattern_match.group(1)).title()
    else:
        country = "World"
    catevent = await edit_or_reply(event, "`collecting data...........`")
    covid = Covid(source="worldometers")
    try:
        country_data = covid.get_status_by_country_name(country)
    except ValueError:
        country_data = ""
    if country_data:
        hmm1 = country_data["confirmed"] + country_data["new_cases"]
        hmm2 = country_data["deaths"] + country_data["new_deaths"]
        data = ""
        data += f"\n⚠️Confirmed   : <code>{hmm1}</code>"
        data += f"\n😔Active           : <code>{country_data['active']}</code>"
        data += f"\n⚰️Deaths         : <code>{hmm2}</code>"
        data += f"\n🤕Critical          : <code>{country_data['critical']}</code>"
        data += f"\n😊Recovered   : <code>{country_data['recovered']}</code>"
        data += f"\n💉Total tests    : <code>{country_data['total_tests']}</code>"
        data += f"\n🥺New Cases   : <code>{country_data['new_cases']}</code>"
        data += f"\n😟New Deaths : <code>{country_data['new_deaths']}</code>"
        await catevent.edit(
            "<b>Corona Virus Info of {}:\n{}</b>".format(country, data),
            parse_mode="html",
        )


CMD_HELP.update(
    {
        "covid": "**Plugin : **`covid`\
        \n\n**Syntax : **`.covid <country name>`\
        \n**Function :** __Get an information about covid-19 data in the given country.__\
        \n\n**Syntax : **`.covid <state name>`\
        \n**Function :** __Get an information about covid-19 data in the given state of India only.__\
        "
    }
)
